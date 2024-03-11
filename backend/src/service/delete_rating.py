from src.api import evaluate
from src.db import firebase_config

def delete_ratings(reservation_id:str, accommodation_id:str):

    firebase_config.db.child("rating").child(accommodation_id).remove()
