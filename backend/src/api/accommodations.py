
import uuid
from fastapi import HTTPException
import db.firebase_config as firebase_config
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


def create_accommodation(accommodation_name, accommodation_loc, 
                         accommodation_bedrooms, accommodation_max_capacity, 
                         accommodation_description, user_id
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
        
        return "Accommodation created successfully!"
    
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
    

