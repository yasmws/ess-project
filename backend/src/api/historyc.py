from fastapi import HTTPException
from  src.db import firebase_config
from datetime import datetime
from src.service.validation import Validation

## ------------- avlidar se checkin < checkout 

def historyc(user_id, checkin, checkout):
    ## validar se user existe

    result = Validation.range_date_validation(checkin, checkout)

    check_in_date = result[1]
    check_out_date = result[2]

    data_atual = datetime.now().date()

    range = data_atual > check_in_date and data_atual >= check_out_date

    exist_user = Validation.get_user_by_id(user_id)
    
    if exist_user and range:

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
            if usuario == user_id and data_user_out['checkout_a'] < data_atual :
                    if data_user_out['checkout_a'] <= data_user_out['checkout_b'] and data_user_in['checkin_a'] >= data_user_in['checkin_b']:
                        result.append(info)
                    else:
                        raise HTTPException(status_code= 400)
        
        if not result:
            raise HTTPException(status_code=404)  
        raise HTTPException(status_code=200, detail = result) 
    raise HTTPException(status_code= 404)