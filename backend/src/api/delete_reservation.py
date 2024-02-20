from fastapi import HTTPException
from  src.db import firebase_config
from datetime import datetime,timedelta
from src.service.validation import Validation
from datetime import datetime, timedelta


def delete_reservation(id_reserva):

    ## verificar se id_resrva existe
    valid = Validation.get_reservation_by_id(id_reserva)
    
    if valid is None:
        print("SIM")
        raise HTTPException(status_code=404, detail="A Reserva não existe no banco de dados")
    print("RESERVA EXISTE NO BANCO")
    try:
        
        accommodation_id = valid['accommodation_id']
        data_in = valid['checkin_date']
        data_out = valid['checkout_date']

        result = Validation.range_date_validation(data_in, data_out)

        current_date = result[1]
        check_out_date = result[2]

        date_now = datetime.strptime( datetime.now().date(), "%Y-%m-%d").date()

        # pegar resulta de check-in e ver se é <= ao dia de hoje
        ## atualizando reservas da acomodação relacionado ao id apagado
        print("oi ola cava")
        if valid['checkin'] <= date_now:
             
            print("testanto testando")
            while current_date <= check_out_date:

                current_date_str = current_date.strftime("%Y-%m-%d")

                firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).update({'disponibility': True, 'reservation_id':"000"})

                current_date += timedelta(days=1)
            
            print("SOMOS INIMIGOS DE QUEM")
            
            firebase_config.db.child("reservation").child(id_reserva).remove()
        
        else:
            print("AQUI")
            return HTTPException(status_code=400, detail= "Período fora de vigência para deletar reserva")
        
        print("oi oi")
        return HTTPException(status_code=200, detail="Reserva deletada com sucesso!")
    except Exception:
        print("TESTE 2")
        raise HTTPException(status_code=400, detail= "Erro ao deletar reserva")
    
