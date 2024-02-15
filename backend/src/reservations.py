import uuid
from fastapi import HTTPException
import src.firebase_config as firebase_config
import src.accommodations as accommodations
from datetime import date, timedelta


def get_price_for_date(accommodation_id, date):
    try:
        # Access the reservations node for the accommodation in Firebase
        reservation_node = firebase_config.db.child("accommodation").child(accommodation_id).child("reservations")

        # Check if the date exists in reservations
        date_info = reservation_node.child(date).get().val()
        if date_info is not None and "price" in date_info:
            price = date_info["price"]
            print("Price:", price)
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
        accommodation = firebase_config.db.child("accommodation").child(accommodation_id).get().val()
        if not accommodation:
            raise HTTPException(status_code=404, detail="Acomodação não encontrada")

        if checkin_date >= checkout_date:
            raise HTTPException(status_code=400, detail="Data de check-out deve ser após a data de check-in")

        # Calculating the total_price
        price = calculate_total_price(accommodation_id, checkin_date, checkout_date) 
        print(price)

        reservation_id = str(uuid.uuid4())  
        reservation_data = {
            "checkin_date": str(checkin_date),  
            "checkout_date": str(checkout_date),
            "total_price": price,
            "client_id": client_id,
            "accommodation_id": accommodation_id,
            "id": reservation_id
        }
        
        ### RESERVATIONS
        
        firebase_config.db.child("reservation").child(reservation_data["id"]).set(reservation_data)
        
        ### ACCOMMODATIONS
         # CHAMAR PARA ATUALIZAR A TABELA DE RESERVAS DA ACOMODAÇÃO
        
        
        return "Reservation created successfully!"
    except HTTPException as e:
        raise e  
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno do servidor") 
        