from fastapi import HTTPException
import firebase_config
import users

import string

def register_user(username):
    try: 
        registered = False
        users = firebase_config.db.child("payment").get().val()
        #print(users)

        for user in users:
            if username == user:
                registered = True

        if registered:
            raise HTTPException(status_code=409, detail="User is already registered!")

        data = {"cnt":0}
        firebase_config.db.child("payment").child(username).set(data)
        return "User registered!"
    
    except HTTPException as hex:
        raise hex

    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


def add_payment_method(username, type, id=None):
    try:        
        #Validate username
        registered = False
        users = firebase_config.db.child("payment").get().val()

        for user in users:
            if username == user:
                registered = True
        
        if not registered:
            raise HTTPException(status_code=404, detail="User not found!")
        
        #Validate type
        if type not in {"pix", "boleto", "debito", "credito"}:
            raise HTTPException(status_code=400, detail="Invalid payment method!")
        
        #Validate type:key association
        if id == None and type not in {"pix", "boleto"}:
            raise HTTPException(status_code=400, detail="This payment method demands a card number.")
        
        elif id != None and type in {"pix", "boleto"}:
            raise HTTPException(status_code=400, detail="This payment method shouldn't feature a card number.")
        
        elif type in {"debito", "credito"}:
            splt_str = id.split()
            
            for string in splt_str:
                if len(string) != 4 or len(splt_str) != 4:
                    raise HTTPException(status_code=400, detail="Stated card number is not valid!")

        #Check if payment method isn't already registered
        cnt = firebase_config.db.child("payment").child(username).child("cnt").get().val()
        
        if cnt != 0:
            for i in range(cnt):
                method = "method" + str(i)
                method_type = firebase_config.db.child("payment").child(username).child(method).child("type").get().val()
                method_id = firebase_config.db.child("payment").child(username).child(method).child("id").get().val()
                
                if method_type == type and method_id == id:
                    raise HTTPException(status_code=409, detail="This payment method is already registered!")

        #Check payment method limit
        cnt = firebase_config.db.child("payment").child(username).child("cnt").get().val()
        
        if cnt == 3:
            raise HTTPException(status_code=400, detail="Payment methods' limit reached!")
        
        #Updating payment method count and registering data 
        cnt += 1
        cnt_s = str(cnt)

        data = {
            "type":type,
            "key":id
        }
        firebase_config.db.child("payment").child(username).child("cnt").set(cnt)
        firebase_config.db.child("payment").child(username).child("method"+cnt_s).set(data)

    except HTTPException as hex:
        raise hex
    
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
