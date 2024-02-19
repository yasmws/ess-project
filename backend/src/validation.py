from fastapi import HTTPException
from src.db import firebase_config 
from datetime import datetime, timedelta

class Validation:

    @staticmethod
    def get_reservation_by_id(reservation_id):
      
        data_rsv = firebase_config.db.child("reservation").child(reservation_id).get().val()
        return data_rsv
    
    @staticmethod
    def get_accommodation_by_id(accommodation_id):
       
        data_acmt = firebase_config.db.child("accommodation").child(accommodation_id).get().val()
        return data_acmt
    @staticmethod
    def get_user_by_id(user_id):
      
        data_user = firebase_config.db.child("users").child(user_id).get().val()
        return data_user
    
    @staticmethod
    
    def range_date_validation(checkin_date, checkout_date):
            
        check_in_date = datetime.strptime(checkin_date, "%Y-%m-%d").date()
        check_out_date = datetime.strptime(checkout_date, "%Y-%m-%d").date()

        data_atual = datetime.now().date()
        range = data_atual < check_in_date and data_atual < check_out_date

        return [range, check_in_date, check_out_date]

    @staticmethod

    def validade_new_user(username, email, cpf):
        users = firebase_config.db.child("users").get().val()
        #Percorre os dados para ver se username, email ou cpf já existem
        for _, info in users.items():
            existing_username = info['username']
            existing_email = info['email']
            existing_cpf = info['cpf']

            if (existing_username == username) or (existing_email == email) or (existing_cpf == cpf):
                return False
        return True
    
    @staticmethod
    def id_has_no_reservation(id_user):
        
        reservations = firebase_config.db.child("reservation").get().val()
        
        for _, info in reservations.items():
            
            disponibilidade = info['client_id']
            
            if  disponibilidade == id_user:
                 return True #existe reserva
        
        return False   #nao existe reserva
    