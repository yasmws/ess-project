from fastapi import HTTPException
from  src.db import firebase_config
from datetime import datetime,timedelta

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
   
    data_rsv = firebase_config.db.child("reservation").child(reservation_id).get().val()
    data_acmt = firebase_config.db.child("accommodation").child(accommodation_id).get().val()
    data_user = firebase_config.db.child("users").child(cliente_id).get().val()

    check_in_date = datetime.strptime(checkin_date, "%Y-%m-%d").date()
    check_out_date = datetime.strptime(checkout_date, "%Y-%m-%d").date()

    data_atual = datetime.now().date()
    range = data_atual < check_in_date and data_atual < check_out_date

    if check_in_date < check_out_date and data_rsv and data_acmt and data_user and range:

        ## checar se a data esta no range correto de disponibilidade
        valid = check_date( accommodation_id, check_in_date, check_out_date, cliente_id)

        if not valid:
            return "Invalid date format"
        try:
            if data_rsv:

            
                date_old = {"checkin": data_rsv["checkin_date"] , "checkout":data_rsv["checkout_date"] }
            
                print("datas antigas", date_old)

                current_date = datetime.strptime(date_old["checkin"], "%Y-%m-%d").date()
                check_out_date = datetime.strptime(date_old["checkout"], "%Y-%m-%d").date()
                price_total = 0.0

                ## limpando datas de acomodação

                while current_date < check_out_date:
                    current_date_str = current_date.strftime("%Y-%m-%d")
                    
                    firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).update({'disponibility': True, 'reservation_id':"000"})
                    price_total += firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).get().val()['price']
                    current_date += timedelta(days=1)
                
                ## setando datas de acomodação
                
                current_date = datetime.strptime(checkin_date, "%Y-%m-%d").date()
                check_out_date = datetime.strptime(checkout_date, "%Y-%m-%d").date()

                while current_date < check_out_date:
                    current_date_str = current_date.strftime("%Y-%m-%d")
                    
                    firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).update({'disponibility': False,  'reservation_id':  reservation_id})
                    
                    # price_total +=  firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).get().val()['price']
            
                    current_date += timedelta(days=1)
                
                if valid == price_total: 
                    firebase_config.db.child("reservation").child(reservation_id).update({"checkin_date" :  checkin_date,"checkout_date":  checkout_date})
                else:
                    return "Date range invalid"
                
               
                return "Reservation updated successfully!"
        
            return f"Não existe reservas para o cliente {cliente_id} na acomodação {data_acmt['name']}" 
            
        except Exception:
            raise HTTPException(status_code=400, detail="Failed to update Reservation.")
    return HTTPException(status_code=400, detail="Invalid fields")     