import uuid
import requests
from fastapi import HTTPException
from starlette import status
import src.db.firebase_config as firebase_config
from datetime import datetime, timedelta

def get_dates_range(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    return dates

def is_valid_user(user_id):
    user = firebase_config.db.child("users").child(user_id).get()
    return user.val() is not None

def create_accommodation(
        accommodation_name,
        accommodation_loc,
        accommodation_bedrooms,
        accommodation_max_capacity,
        accommodation_description,
        user_id
    ):
        try: 
            accommodation_id = str(uuid.uuid4())  # Generate accommodation ID
        
            data = {
                "id": accommodation_id,
                "name": accommodation_name,
                "location": accommodation_loc,
                "bedrooms": accommodation_bedrooms,
                "max_capacity": accommodation_max_capacity,
                "description": accommodation_description,
                "user_id": user_id 
            }
            
            # Validation of data
            
            # Is the name within 20 characters?
            if len(accommodation_name) > 20:
                raise ValueError("Accommodation name must be 20 characters or less.")
            
            # Is the accommodation_bedrooms a number bigger than 0?
            if not isinstance(accommodation_bedrooms, int) or accommodation_bedrooms <= 0:
                raise ValueError("Number of bedrooms must be a positive integer.")
            
            # Is the accommodation_max_capacity a number equal or bigger than the accommodation_bedrooms?
            # And is the number bigger than 0?
            if not isinstance(accommodation_max_capacity, int) or accommodation_max_capacity <= 0:
                raise ValueError("Max capacity must be a positive integer.")
            if accommodation_max_capacity < accommodation_bedrooms:
                raise ValueError("Max capacity must be equal or greater than the number of bedrooms.")
            
            # Is the description within 400 characters?
            if len(accommodation_description) > 400:
                raise ValueError("Description must be 400 characters or less.")
            
            # Does the user_id exist in our database? (You should implement this validation)
            if not is_valid_user(user_id):
                raise ValueError("Invalid user ID.")
            
            # Store accommodation data in Firebase
            firebase_config.db.child("accommodation").child(data["id"]).set(data)
            
            # Disponibility calendar for the accommodation
            today = datetime.today()
            end_date = today + timedelta(days=365)
            data_reservation = {
                "price": 1.0,
                "disponibility": True,
                "reservation_id": "000" # Gambiarrra, a discutir
            }  
            
            initial_daily_prices = {date: data_reservation for date in get_dates_range(today, end_date)}
            firebase_config.db.child("accommodation").child(data["id"]).child("reservations").set(initial_daily_prices)
            
            return HTTPException(status_code=200, detail="Accommodation created successfully!")
    
        except ValueError as ve:
            raise HTTPException(status_code=400, detail=str(ve))
            
        except Exception as e:
            raise HTTPException(status_code=400, detail="Failed to create accommodation.")

def update_reservation_info(accommodation_id, default_price=0.0, disponibility=False):
    try:
        today = datetime.today()
        end_date = today + timedelta(days=365)
        reservation_node = firebase_config.db.child("accommodation").child(accommodation_id).child("reservations")
        
        # Loop através de cada data no intervalo de datas
        for date in get_dates_range(today, end_date):
            # Verifica se a disponibilidade para esta data é False
            if not reservation_node.child(date).child("disponibility").get().val():
                # Atualiza as informações de reserva apenas se a disponibilidade for False
                reservation_info = {
                    "price": default_price,
                    "disponibility": disponibility,
                }
                reservation_node.child(date).update(reservation_info)
        
        return "Reservation info updated successfully!"
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to update reservation info.")

def get_accommodations(
        location: str = None,
        checkin: datetime = None,
        checkout: datetime = None,
        guests: int = None
    ):
    try:
        accommodations = firebase_config.db.child("accommodation").order_by_child("location")        
        accommodations = accommodations.limit_to_first(10).get()  # Adjust the limit as needed
        
        accommodations_list = []

        for accommodation in accommodations.each():
            accommodation_data = accommodation.val()
            
            # Check whether the image exists or not on the server
            img_url = firebase_config.storage.child(f'accommodation/{accommodation_data["id"]}.jpg').get_url(None)
            r = requests.head(img_url)
            fileExists = (r.status_code == requests.codes.ok)
            
            if fileExists:
                accommodation_data["image"] = img_url
            else:
                accommodation_data["image"] = firebase_config.storage.child("accommodation/house.jpg").get_url(None)
            
            if location and location.lower() not in accommodation_data["location"].lower():
                continue
            
            if guests and guests > accommodation_data["max_capacity"]:
                continue
            
            if checkin and checkout:
                dates = get_dates_range(checkin, checkout)
                for date in dates:
                    if not accommodation_data["reservations"][date]["disponibility"]:
                        break
                else:
                    accommodations_list.append(accommodation_data)
            else:
                accommodations_list.append(accommodation_data)

        accommodations_list = [
            {
                "name": accommodation["name"],
                "id": accommodation["id"],
                "description": accommodation["description"],
                "bedrooms": accommodation["bedrooms"],
                "location": accommodation["location"],
                "max_capacity": accommodation["max_capacity"],
                "image": accommodation["image"]
            }
            for accommodation in accommodations_list
        ]

        if not accommodations_list:
            return status.HTTP_204_NO_CONTENT
        return accommodations_list
    except Exception:
        raise HTTPException(status_code=400, detail="Failed looking for accommodations.")
    
def get_accommodation_by_id(accommodation_id):
    try:
        accommodation_data = firebase_config.db.child("accommodation").child(accommodation_id).get().val()
        
        img_url = firebase_config.storage.child(f'accommodation/{accommodation_data["id"]}').get_url(None)
        r = requests.head(img_url)
        fileExists = (r.status_code == requests.codes.ok)
        if fileExists:
            accommodation_data["image"] = img_url
        else:
            accommodation_data["image"] = firebase_config.storage.child("accommodation/house.jpg").get_url(None)
        
        if not accommodation_data:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Accommodation not found")
        
        return accommodation_data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Failed looking for accommodations. {str(e)}")
