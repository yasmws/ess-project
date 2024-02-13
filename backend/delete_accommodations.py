from fastapi import HTTPException
import firebase_config as firebase_config


def delet_accommodation(accommodation_id):

    try:
        accomodation_by_id = firebase_config.child("accommodation").child(accommodation_id).get()

        if accomodation_by_id is None:
            raise HTTPException(status_code=404, detail="Accommodation not found.")
        
        firebase_config.child("accommodation").child(accommodation_id).remove()
        return "Accommodation deleted with success!"
    except Exception:
         raise HTTPException(status_code=400, detail="Failed to delete accommodation.")
    
# Quando deleter tem que atualizar em outros cantos
