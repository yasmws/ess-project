from fastapi import HTTPException
import firebase_config as firebase_config
from datetime import datetime,timedelta

## Política de auteração de data: Desde que o intervalo de dias seja igual ao da reserva inicial
## editar mesma quantidade de dias (Referente ao pagamento)

def check_date(accommodation_id, checkin_date, checkout_date, client_id):

    ## checar range escolhido (Se há disponibilidade)

    check_in_date = datetime.strptime(checkin_date, "%Y-%m-%d").date()
    check_out_date = datetime.strptime(checkout_date, "%Y-%m-%d").date()
    
    current_date = check_in_date

    while current_date <= check_out_date:

        # O RANGE PODE ESTAR OCUPADO, PELA PRÓPRIA PESSOA E 
        current_date_str = current_date.strftime("%Y-%m-%d")
        result = firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).get().val()

        id =  firebase_config.db.child("reservation").child(result['reservation_id']).get().val()['client_id']
        ## além de ver se eh falso, tem que verificar se não é a própria pessoa que reservou
        if result['disponibility'] is False and id is not client_id:
            print("fora do range de disponibilidade")
            return False
        current_date = timedelta(days=1)

    ## verificar se datas são maiores do que atualidade
    
    data_atual = datetime.now()
    data_formatada = data_atual.strftime('%Y-%m-%d')
    
    if data_formatada <= check_in_date and data_formatada <= check_out_date:
        return True
    
    return False

def edit_reservation( reservation_id, checkin_date, checkout_date, accommodation_id, cliente_id):
 
    data_reservation = firebase_config.db.child("reservation").child(reservation_id).get().val()

    ## checar se a data esta no range correto de disponibilidade
    valid = check_date( accommodation_id, checkin_date, checkout_date, cliente_id)

    if not valid:
        return "Invalid date format"
    try:
        if data_reservation:

            check_in_date = datetime.strptime(checkin_date, "%Y-%m-%d").date()
            check_out_date = datetime.strptime(checkout_date, "%Y-%m-%d").date()

            if check_out_date > check_in_date:
                date_old = {"checkin":data_reservation["checkin_date"] , "checkout":data_reservation["checkout_date"] }
               
                print("datas antigas", date_old)
                current_date = datetime.strptime(date_old["checkin"], "%Y-%m-%d").date()
                check_out_date = datetime.strptime(date_old["checkout"], "%Y-%m-%d").date()
                price_total = 0.0

                ## limpando datas de acomodação

                while current_date <= check_out_date:
                    current_date_str = current_date.strftime("%Y-%m-%d")
                    
                    firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).update({'disponibility': True, 'reservation_id':"000"})
                    current_date += timedelta(days=1)
                
                ## setando datas de acomodação
                
                current_date = datetime.strptime(checkin_date, "%Y-%m-%d").date()
                check_out_date = datetime.strptime(checkout_date, "%Y-%m-%d").date()

                while current_date <= check_out_date:
                    current_date_str = current_date.strftime("%Y-%m-%d")
                    
                    firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).update({'disponibility': False,  'reservation_id':  reservation_id})
                    
                    price_total +=  firebase_config.db.child("accommodation").child(accommodation_id).child("reservations").child(current_date_str).get().val()['price']
            
                    current_date += timedelta(days=1)
                
                firebase_config.db.child("reservation").child(reservation_id).update({"checkin_date" :  checkin_date,"checkout_date":  checkout_date, "total_price": price_total})

                return  "Reservation edited successfully!"
            
            return HTTPException(status_code=400, detail="Data de check-out deve ser após a data de check-in")
        
        accomodation_name = firebase_config.db.child("accommodation").child(accommodation_id).get().val()["name"]

        return f"Não existe reservas para o cliente {cliente_id} na acomodação {accomodation_name}" 
        
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to update Reservation.")
        