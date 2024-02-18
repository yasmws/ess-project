from fastapi import HTTPException
import firebase_config
import users

def add_payment_method(username, type, key):
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
        if type not in {"pix", "debito", "credito"}:
            raise HTTPException(status_code=400, detail="Invalid payment method!")

        #Check payment method limit
        cnt = firebase_config.db.child("payment").child(username).child("cnt").get().val()
        if cnt == 3:
            raise HTTPException(status_code=400, detail="Payment methods' limit reached!")
        cnt += 1
        cnt_s = str(cnt)

        data = {
            "type":type,
            "key":key
        }
        firebase_config.db.child("payment").child(username).child("cnt").set(cnt)
        firebase_config.db.child("payment").child(username).child("method"+cnt_s).set(data)

    except HTTPException as hex:
        raise hex
    
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

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


