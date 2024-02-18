from fastapi import HTTPException
from  src.db import firebase_config
from datetime import datetime,timedelta
from src.service.validation import Validation


def delete_reservation(id_reserva):

    ## verificar se id_resrva existe
    valid = Validation.get_reservation_by_id(id_reserva)
    
    if valid is None:
         raise HTTPException(status_code=404, detail="A Reserva não existe no banco de dados")
    
    try:
        
        accommodation_id = valid['accommodation_id']
        data_in = valid['checkin_date']
        data_out = valid['checkout_date']

        result = Validation.range_date_validation(data_in, data_out)

        current_date = result[1]
        check_out_date = result[2]

        ## atualizando reservas da acomodação relacionado ao id apagado
        while current_date < check_out_date:

            current_date_str = current_date.strftime("%Y-%m-%d")

            firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).update({'disponibility': True, 'reservation_id':"000"})

            current_date += timedelta(days=1)
        
        firebase_config.db.child("reservation").child(id_reserva).remove()

        return HTTPException(status_code=200, detail="Reserva deletada com sucesso!")
    except Exception:
        raise HTTPException(status_code=400, detail= "Erro ao deletar reserva")
    
