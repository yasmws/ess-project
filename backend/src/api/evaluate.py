from fastapi import HTTPException
import db.firebase_config as firebase_config

def add_rating(reservation_id:str, stars:int, comment:str, accommodation_id:str):
    if(not_exist_rating(reservation_id, accommodation_id)):
        if stars <= 5 and stars > 0:
            data = {
                "reservation_id" : reservation_id,
                "stars": stars,
                "comment": comment,
                "accommodation_id": accommodation_id,
            }
            firebase_config.db.child("rating").child(data["accommodation_id"]).push(data)
            return "User rating added successfully!"
        else:
            raise HTTPException(status_code=500, detail="the number of stars is not in the allowed range.")
    else:
            raise HTTPException(status_code=500, detail="it already has an evaluation in rating table")

# busca a informção de que aquela reserva já tem uma avaliação
def not_exist_rating(reservation_id:str, accommodation_id:str):
    try:
        exist = firebase_config.db.child("rating").child(accommodation_id).order_by_child("reservation_id").equal_to(reservation_id).get()
        print(exist.val())
        if exist.val() == []:
            return True
        else:
            return False
    except Exception:
        raise HTTPException(status_code=500, detail="Failed get exitence information.")
