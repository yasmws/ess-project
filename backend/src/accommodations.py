import uuid
from fastapi import HTTPException
import src.firebase_config as firebase_config
from datetime import datetime, timedelta

"""
Publicar Acomodacoes:
- Criar acomodacoes
- Deletar acomodacoes
- Atualizar disponibilidade
"""

def get_dates_range(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    return dates


def create_accommodation(accommodation_name, accommodation_loc, 
                         accommodation_bedrooms, accommodation_max_capacity, 
                         accommodation_description):
    try: 
        accommodation_id = str(uuid.uuid4())  # Generate accommodation ID
        
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
        
        # Create an initial daily prices calendar for the accommodation
        today = datetime.today()
        end_date = today + timedelta(days=365)
        default_price = 0.0  
        initial_daily_prices = {str(date): default_price for date in get_dates_range(today, end_date)}
        firebase_config.db.child("accommodation").child(data["id"]).child("reservations").set(initial_daily_prices)
        
        return "Accommodation created successfully!"
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to create accommodation.")


def delete_accommodation(accommodation_id):
    try:
        firebase_config.db.child("accommodation").child(accommodation_id).remove()
        return "Accommodation deleted successfully!"
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to delete accommodation.")
    
#def modify_prices_accommodation(accommodation_id):
#    try:
        
