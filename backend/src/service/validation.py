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
        
        ## aqui deveria ser pra comparar se as datas estão certos, em questão de range
        if (data_atual < check_in_date) and (check_in_date < check_out_date):
            range = True
        else:
            range = False

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
    def id_has_reservation(id_user):
        
        reservations = firebase_config.db.child("reservation").get().val()
        
        for _, info in reservations.items():
            
            disponibilidade = info['client_id']
            
            if  disponibilidade == id_user:
                 return True #existe reserva
        
        return False   #nao existe reserva
    
    @staticmethod
    def user_reservation(id_user):
        
        reservations = firebase_config.db.child("reservation").get().val()
        
        for index, info in reservations.items():
            
            user_teste = info['client_id']
            
            if  user_teste == id_user:
                 firebase_config.db.child("reservation").child(index).remove()
        
        return True
    
    @staticmethod
    def validate_user_payment_register(username):
        users = firebase_config.db.child("payment").get().val()

        for user in users:
            if username == user:
                return True
            
        return False
    
    @staticmethod
    def get_methods_amount(username):
        cnt = firebase_config.db.child("payment").child(username).child("cnt").get().val()
        return cnt
    
    @staticmethod
    def validate_method_refer(username, method_refer):
        methods = firebase_config.db.child("payment").child(username).get().val()

        for method in methods:
            if method == method_refer:
                return True
            
        return False
    
    @staticmethod
    def validate_method_register(username, method_type, method_id):
        cnt = firebase_config.db.child("payment").child(username).child("cnt").get().val()

        for i in range(cnt):
            method = firebase_config.db.child("payment").child(username).child("method"+str(i+1))
            if method_type == method.child("type").get().val() and method_id == method.child("id").get().val():
                return True
        
        return False
    