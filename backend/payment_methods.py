from fastapi import HTTPException
import firebase_config
import users

#fix def add_payment_method(username, type, key, cnt):
#    try:
#
#    except:

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


