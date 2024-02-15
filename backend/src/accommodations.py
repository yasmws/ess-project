import uuid
from fastapi import HTTPException
import src.firebase_config as firebase_config
from datetime import datetime, timedelta

def get_dates_range(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    return dates


def create_accommodation(accommodation_name, accommodation_loc, 
                         accommodation_bedrooms, accommodation_max_capacity, 
                         accommodation_description
                        ):
    try: 
        accommodation_id = str(uuid.uuid4())  # Generate accommodation ID
        date = date
        data = {
            "name": accommodation_name,
            "location": accommodation_loc,
            "bedrooms": accommodation_bedrooms,
            "max_capacity": accommodation_max_capacity,
            "description": accommodation_description,
            "id": accommodation_id
        }
        # Store accommodation data in Firebase
        firebase_config.db.child("accommodation").child(data["id"]).set(data)
        
        # Disponibility calendar for the accommodation
        today = datetime.today()
        end_date = today + timedelta(days=365)
        data_reservation = {
            "price": 1.0,
            "disponibility": False,
            "reservation_id": None
        }  
        initial_daily_prices = {str(date): data_reservation for date in get_dates_range(today, end_date)}
        
        
        firebase_config.db.child("accommodation").child(data["id"]).child("reservations").set(initial_daily_prices)
        
        return "Accommodation created successfully!"
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
