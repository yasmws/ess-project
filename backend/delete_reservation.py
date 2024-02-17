from fastapi import HTTPException
import firebase_config as firebase_config
from datetime import datetime,timedelta


def delete_reservation(id_reserva):

    ## verificar se id_resrva existe
    valid = firebase_config.db.child("reservation").child(id_reserva).get().val()
    
    if valid is None:
         raise HTTPException(status_code=404, detail="Reservation don't exists")
    
    try:
        result = firebase_config.db.child("reservation").child(id_reserva).get().val()

        accommodation_id = result['accommodation_id']
        data_in = result['checkin_date']
        data_out = result['checkout_date']

        current_date = datetime.strptime(data_in, "%Y-%m-%d").date()
        check_out_date = datetime.strptime(data_out, "%Y-%m-%d").date()

        ## atualizando reservas da acomodação relacionado ao id apagado
        while current_date <= check_out_date:

            current_date_str = current_date.strftime("%Y-%m-%d")

            firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).update({'disponibility': True, 'reservation_id':"000"})

            current_date += timedelta(days=1)
        
        firebase_config.db.child("reservation").child(id_reserva).remove()
        return  "Reservation was deleted"
    except Exception:
            raise HTTPException(status_code=400, detail= "Erro ao deletar reserva")
    
