from fastapi import HTTPException
from src.db import firebase_config


def register_user(username):
    data = {"cnt":0}
    firebase_config.db.child("payment").child(username).set(data)
    return "User registered!"

def validate_user_payment_register(username):
    users = firebase_config.db.child("payment").get().val()

    for user in users:
        if username == user:
            return True
        
    return False

def validate_payment_method_register(username, method):
    methods = firebase_config.db.child("payment").child(username).get().val()

    for reg_method in methods:
        if method == reg_method:
            return True
        
    return False

def validate_method_type(type):
    if type in {"pix", "boleto", "debito", "credito"}:
        return True
    
    return False

def validate_type_and_id(type, id):
    if id == None and type not in {"pix", "boleto"}:
        return False
        
    elif id != None and type in {"pix", "boleto"}:
        return False
    
    return True

def validate_id_format(type, id):
    if type in {"debito", "credito"}:
        splt_str = id.split()

        for string in splt_str:
            if len(string) != 4 or len(splt_str) != 4:
                return False
            
    return True

def check_payment_methods_limit(username):
    cnt = firebase_config.db.child("payment").child(username).child("cnt").get().val()
        
    if cnt == 3:
        return False
    
    return True

def is_paymet_method_registered(username, type, id):
    cnt = firebase_config.db.child("payment").child(username).child("cnt").get().val()
        
    if cnt != 0:
        for i in range(cnt+1):
            method = "method" + str(i)
            method_type = firebase_config.db.child("payment").child(username).child(method).child("type").get().val()
            method_id = firebase_config.db.child("payment").child(username).child(method).child("id").get().val()

            if method_id == id and id == None and method_type == type:
                return "method registered"
            elif method_id == id and id != None:
                return "id registered"
            
    return None

def add_payment_method(username, type, id):
    try:        
        #Validate username
        if not validate_user_payment_register(username):
            raise HTTPException(status_code=404, detail="User not found!")
        
        #Validate type
        if not validate_method_type(type):
            raise HTTPException(status_code=400, detail="Invalid payment method!")
        
        #Validate type:id association
        if not validate_type_and_id(type, id):
            raise HTTPException(status_code=400, detail="The id number is incompatible with this payment method!")
        
        #Validate id number format
        if not validate_id_format(type, id):
            raise HTTPException(status_code=400, detail="Stated id number is not valid!")

        #Check if payment method is already registered
        error = is_paymet_method_registered(username, type, id)

        if error == "method registered":
            raise HTTPException(status_code=409, detail="This payment method is already registered!")
        elif error == "id registered":
            raise HTTPException(status_code=409, detail="There is already a registered payment method with this id.")

        #Check payment method limit        
        if not check_payment_methods_limit(username):
            raise HTTPException(status_code=400, detail="Payment methods' limit reached!")
        
        #Updating payment method count and registering data 
        cnt = firebase_config.db.child("payment").child(username).child("cnt").get().val()
        cnt += 1
        cnt_s = str(cnt)

        data = {
            "type": type,
            "id": id
        }
        firebase_config.db.child("payment").child(username).child("cnt").set(cnt)
        firebase_config.db.child("payment").child(username).child("method"+cnt_s).set(data)

        return HTTPException(status_code=200, detail="Payment method added!")

    except HTTPException as hex:
        raise hex
    
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    

def update_payment_method(username, method, type, id):
    try:
        cur_id = firebase_config.db.child("payment").child(username).child(method).child("id").get().val()
        cur_type = firebase_config.db.child("payment").child(username).child(method).child("type").get().val()

        if type == "foo":
            type = cur_type
        if id == "foo":
            id = cur_id

        #Validate username
        if not validate_user_payment_register(username):
            raise HTTPException(status_code=404, detail="User not found!")
        
        #Validate method
        if not validate_payment_method_register(username, method):
            raise HTTPException(status_code=404, detail="Payment method not found!")
        
        #Validate type
        if not validate_method_type(type):
            raise HTTPException(status_code=400, detail="Invalid payment method!")
        
        #Check if payment method is already registered
        error = is_paymet_method_registered(username, type, id)

        if error == "method registered":
            raise HTTPException(status_code=409, detail="This payment method is already registered!")
        elif error == "id registered":
            raise HTTPException(status_code=409, detail="There is already a registered payment method with this id.")

        #Validate update
        if type in {"debito", "credito"}:
            if id == None:
                raise HTTPException(status_code=400, detail="This payment method demands an id number.")
            
            else:
                splt_str = id.split()

                for string in splt_str:
                    if len(string) != 4 or len(splt_str) != 4:
                        raise HTTPException(status_code=400, detail="Stated id number is not valid!")

                data = {"type": type,
                        "id": id}
                
        else:
            data = {"type": type,
                    "id": None}
        
        firebase_config.db.child("payment").child(username).child(method).set(data)

        return HTTPException(status_code=200, detail="Payment method updated!")

    except HTTPException as hex:
        raise hex
    
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


def delete_payment_method(username, method):
    try:
        #Validate username
        if not validate_user_payment_register(username):
            raise HTTPException(status_code=404, detail="User not found!")
        
        #Validate method
        if not validate_payment_method_register(username, method):
            raise HTTPException(status_code=404, detail="Payment method not found!")
        
        #Deletion
        iter = int(method.removeprefix("method"))
        cnt = firebase_config.db.child("payment").child(username).child("cnt").get().val()

        for i in range(cnt-iter):
            cur_i = iter + i
            if (cur_i) < cnt:
                data = firebase_config.db.child("payment").child(username).child("method"+str(cur_i+1)).get().val()
                firebase_config.db.child("payment").child(username).child("method"+str(cur_i)).update(data)
        
        firebase_config.db.child("payment").child(username).child("method"+str(cnt)).set({})
        cnt -= 1
        firebase_config.db.child("payment").child(username).update({"cnt": cnt})

        return HTTPException(status_code=200, detail="Payment method deleted!")

    except HTTPException as hex:
        raise hex
    
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    