from fastapi import HTTPException
from  src.db import firebase_config
from datetime import datetime,timedelta
from src.service.validation import Validation
## Política de auteração de data: Desde que o intervalo de dias seja igual ao da reserva inicial
## editar mesma quantidade de dias (Referente ao pagamento)


def check_date(accommodation_id, checkin_date, checkout_date, client_id):

    ## checar range escolhido (Se há disponibilidade)
    current_date = checkin_date
    price = 0

    while current_date < checkout_date:

        current_date_str = current_date.strftime("%Y-%m-%d")
        result = firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).get().val()

        if result['reservation_id'] != "000":
            id =  firebase_config.db.child("reservation").child(result['reservation_id']).get().val()['client_id']
            if result['disponibility'] == False and id != client_id:
                return False
            
        current_date += timedelta(days=1)
        price += result['price']

    return price

def edit_reservation( reservation_id, checkin_date, checkout_date, accommodation_id, cliente_id):

    ## Validação das entradas
   
    data_rsv = Validation.get_reservation_by_id(reservation_id)
    data_acmt = Validation.get_accommodation_by_id(accommodation_id)
    data_user = Validation.get_user_by_id(cliente_id)


    result = Validation.range_date_validation(checkin_date, checkout_date)

    check_in_date = result[1]
    check_out_date = result[2]

    if check_in_date < check_out_date and data_rsv and data_acmt and data_user and result[0]:
        
        ## checar se existe aquela reserva na acomodação
        if data_rsv['accommodation_id'] != accommodation_id:
            raise HTTPException(status_code=404, detail=f"Não existe reserva para acomodação {data_acmt['name']}")
        
        ## checar se a data esta no range correto de disponibilidade
        valid = check_date( accommodation_id, check_in_date, check_out_date, cliente_id)

        if not valid:
           raise HTTPException(status_code=400, detail="Invalid Format")
        
        try:
            results = Validation.range_date_validation(data_rsv["checkin_date"], data_rsv["checkout_date"])

            current_date = results[1]
            

            price_total = 0.0

            ## limpando datas de acomodação
           
            while current_date < results[2]:

                current_date_str = current_date.strftime("%Y-%m-%d")
                
                firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).update({'disponibility': True, 'reservation_id':"000"})
                price_total +=firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).get().val()['price']
                
                current_date += timedelta(days=1)
            
            ## setando datas de acomodação
            
            current_date = result[1]
            check_out_date = result[2]

            while current_date < check_out_date:
                current_date_str = current_date.strftime("%Y-%m-%d")
                
                firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).update({'disponibility': False,  'reservation_id':  reservation_id})
                current_date += timedelta(days=1)
    
            if valid == price_total: 
                firebase_config.db.child("reservation").child(reservation_id).update({"checkin_date" :  checkin_date,"checkout_date":  checkout_date})
            else:
                return HTTPException(status_code=400, detail="Date Range invalid") 
            return HTTPException(status_code=200, detail="Reservation updated successfully!")
    
        except Exception:
            raise HTTPException(status_code=400, detail="Failed to update Reservation.")
    raise HTTPException(status_code=400, detail="Invalid fields")     