import uuid
from fastapi import HTTPException
import src.firebase_config as firebase_config
import src.accommodations as accommodations
from datetime import timedelta, datetime

def is_valid_date(date_str):
    try:
        year, month, day = map(int, date_str.split('-'))
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day > 29:
                    return False
            elif day > 28:
                return False
        return True
    except ValueError:
        return False


def get_price_for_date(accommodation_id, date):
    try:
        # Access the reservations node for the accommodation in Firebase
        reservation_node = firebase_config.db.child("accommodation").child(accommodation_id).child("reservations")

        # Check if the date exists in reservations
        date_info = reservation_node.child(date).get().val()
        if date_info is not None and "price" in date_info:
            price = date_info["price"]
            #print("Price:", price)
            return price
        else:
            print("Price not found for the given date:", date)
            return None

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error!")


def calculate_total_price(accommodation_id, checkin_date, checkout_date):
    try:
        total_price = 0.0
        current_date = checkin_date
        
        while current_date < checkout_date:
            # Obtém o preço para o dia atual
            price = get_price_for_date(accommodation_id, current_date)
            # Adiciona o preço do dia ao preço total
            total_price += price
            # Avança para o próximo dia
            current_date += timedelta(days=1)
        return total_price
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno do servidor")
    
    
    
def create_reservation(client_id, accommodation_id, checkin_date, checkout_date):
    try:
        # Validation
        
        ## Are the checkin_date and the checkout_date in the YYYY-mm-dd format?
        if not is_valid_date(str(checkin_date)):
            raise HTTPException(status_code=400, detail="Invalid check-in date format. Please use YYYY-mm-dd")

        if not is_valid_date(str(checkout_date)):
            raise HTTPException(status_code=400, detail="Invalid check-out date format. Please use YYYY-mm-dd")
        
        ## Does the client_id exist?
        if not accommodations.is_valid_user(client_id):
            raise HTTPException(status_code=404, detail="Client not found")
        
        ## Does the accommodation_id exist?
        accommodation = firebase_config.db.child("accommodation").child(accommodation_id).get().val()
        if not accommodation:
            raise HTTPException(status_code=404, detail="Accommodation not found")
        
        ## Is the client_id not the same person that created the accommodation?
        if client_id == accommodation["user_id"]:
            raise HTTPException(status_code=400, detail="Client cannot reserve their own accommodation")
        
        ## Is the checkin not before today?
        if checkin_date < datetime.today().date():
            raise HTTPException(status_code=400, detail="Check-in date cannot be in the past")
        
        ## Is the checkin before the checkout?
        if checkin_date >= checkout_date:
            raise HTTPException(status_code=400, detail="Check-out date must be after check-in date")
        
        ## Are the chosen days still available?
        current_date = checkin_date
        check_out_date = checkout_date
        while current_date <= check_out_date:
            current_date_str = str(current_date)
            dis = firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).get().val().get("disponibility")
            # print(dis)
            if dis == False:
                raise HTTPException(status_code=400, detail="Chosen date already reserved")
            current_date += timedelta(days=1)

        # Calculating the total_price
        price = calculate_total_price(accommodation_id, checkin_date, checkout_date) 
        #print(price)

        reservation_id = str(uuid.uuid4())  
        reservation_data = {
            "checkin_date": str(checkin_date),  
            "checkout_date": str(checkout_date),
            "client_id": client_id, 
            "accommodation_id": accommodation_id, 
            "reservation_id": reservation_id, 
            "total_price": price
        }
    
        ### RESERVATIONS
        
        # Add the reservation_data into the reservation 
        firebase_config.db.child("reservation").child(reservation_id).set(reservation_data)
        
        ### ACCOMMODATIONS
        
        # Update the reservation table inside the accommodation
        current_date = checkin_date
        check_out_date = checkout_date
        while current_date <= check_out_date:
            current_date_str = str(current_date)
            firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).update({'disponibility': False, 'reservation_id': reservation_id})  # Removed the unusual character after 'disponibility':
            current_date += timedelta(days=1)
            
        return "Reservation created successfully! Total: {}".format(price)

    except HTTPException as he:
        raise he
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

        
