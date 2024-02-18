from fastapi import HTTPException
import firebase_config
import users

#def add_payment_method(username, type, key, cnt):
#    try:
#
#    except:

def register_user(username):
    try: 
        registered = False
        users = firebase_config.db.child("payment")
        for user in users:
            if username == user["username"]:
                registered = True
        if not registered:
            data = {"cnt":0}
            firebase_config.db.child("payment").child(username).set(data)
    except Exception:
        raise HTTPException(status_code=409,detail="Usuário já está registrado!")


