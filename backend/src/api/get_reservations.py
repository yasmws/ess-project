from fastapi import HTTPException
import src.db.firebase_config as firebase_config
from datetime import datetime, timedelta

storage = firebase_config.firebase.storage()

def get_reservations(id_client):
    
    result = []
    try:
        reservation_node = firebase_config.db.child("reservation").get().val()

        for _, info in reservation_node.items():


            if info['client_id'] == id_client:

                checkin = datetime.strptime( info['checkin_date'], "%Y-%m-%d").date()

                data_atual = datetime.now().date()

                if checkin >= data_atual:
               
                    image_url = storage.child("accommodation").child("be7cf4d8-f408-41e7-85f2-920b5be751c4").get_url(None)
                    accomodation = firebase_config.db.child("accommodation").child(info['accommodation_id']).get().val()
                    
                    obj = {'name': accomodation['name'], 'location': accomodation['location'], 'id': info['reservation_id'], 
                        'img_url': image_url, 'price': info['total_price'], 'checkin': info['checkin_date'], 'checkout': info['checkout_date'],
                         'accommodation_id': info['accommodation_id']}
                    result.append(obj)

        return  HTTPException(status_code=200, detail=result)
        
    except Exception:
        raise HTTPException(status_code=400, detail="Erro interno do servidor")
