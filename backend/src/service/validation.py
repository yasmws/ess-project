from fastapi import HTTPException
from src.db import firebase_config 
from datetime import datetime, timedelta

class Validation:

    @staticmethod
    def get_reservation_by_id(reservation_id):
      
        data_rsv = firebase_config.db.child("reservation").child(reservation_id).get().val()
        print("data_rsv", data_rsv)
        return data_rsv
    
    @staticmethod
    def get_accommodation_by_id(accommodation_id):
       
        data_acmt = firebase_config.db.child("accommodation").child(accommodation_id).get().val()
        return data_acmt
    @staticmethod
    def get_user_by_id(user_id):
      
        data_user = firebase_config.db.child("users").child(user_id).get().val()
        return data_user