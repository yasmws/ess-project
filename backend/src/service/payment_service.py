from fastapi import HTTPException
import firebase_config


class PaymentService:

    @staticmethod
    def get_user(username):
        data = firebase_config.db.child("payment").child(username).get().val()
        return data