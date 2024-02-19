from fastapi import HTTPException
import firebase_config as firebase_config

def create_user(email, password, name, username, cpf):
    try:
        firebase_config.auth.create_user_with_email_and_password(email, password)

        print("User created")
        data = {
            "name": name,
            "email": email,
            "cpf": cpf,
            "username": username,
        }
        firebase_config.db.child("users").child(data["username"]).set(data)
        print("User data added successfully!")
        return "User created!"
    except Exception:
        raise HTTPException(status_code=400, detail="It was not possible to create the user.")

def login_user(email, password):
    try:
        firebase_config.auth.sign_in_with_email_and_password(email, password)
        return "User logged in!"
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid email or password.")