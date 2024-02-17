from fastapi import HTTPException
import firebase_config as firebase_config
from datetime import datetime, timedelta


def historyc(user_id, checkin, checkout):
    ## validar se user existe
    exist_user = firebase_config.db.child("users").child(user_id).get().val()
    if exist_user:

        reservation = firebase_config.db.child("reservation").get().val()
        data_atual = datetime.now().date()  
        result = []
        
        for _, info in reservation.items():
            usuario = info['client_id']
           
            data_user_in = { 'checkin_a': datetime.strptime(info['checkin_date'], "%Y-%m-%d").date(),
                            'checkin_b':  datetime.strptime(checkin, "%Y-%m-%d").date()}
           
            data_user_out = { 'checkout_a': datetime.strptime(info['checkout_date'], "%Y-%m-%d").date(),
                            'checkout_b':  datetime.strptime(checkout, "%Y-%m-%d").date()}
            
            ## está funcioanndo. Porém, para teste colocar  <= em data_atual

            if usuario == user_id and data_user_out['checkout_a'] < data_atual and data_user_in['checkin_a'] <= data_user_out['checkout_a']:
                    print("passei")
                    if data_user_out['checkout_a'] <= data_user_out['checkout_b'] and data_user_in['checkin_a'] >= data_user_in['checkin_b']:
                        result.append(info)
                    else:
                        raise HTTPException(status_code= 400, detail="Date interval not valid")
        
        if not result:
            raise HTTPException(status_code=200, detail = result)  
        raise HTTPException(status_code=200, detail = result) 
    raise HTTPException(status_code= 404, detail=f"{user_id} not exist")
