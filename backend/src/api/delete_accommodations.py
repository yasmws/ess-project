from fastapi import HTTPException
from  src.db import firebase_config
from src.service.validation import Validation

def check_any_reservation(accommodation_id):
        
        reservations = firebase_config.db.child("accommodation").child(accommodation_id).child("reservations")

        reservations = reservations.get().val()
        
        ## percorre todas as datas (false -> tem clientes / true-> disponível/sem cliente)
        for _, info in reservations.items():
            
            disponibilidade = info['disponibility']
            if not disponibilidade:
                 return True #existe reserva
        
        return False   #nao existe reserva
        


def delet_accommodation(accommodation_id):

    ## passou no teste de ter acomodações
   
    # validação
    ## ver se id de acomodação existe
    if Validation.get_accommodation_by_id(accommodation_id):
         
         raise HTTPException(status_code=404, detail="The accomodation not exist")
    
    valid = check_any_reservation(accommodation_id)
    ## ver se id de acomodação não tem acomodação
    if valid:
        raise HTTPException(status_code=404, detail="Can't delet an accommodation with reservations")
        #return "Can't delet an accommodation with reservations"
    
    try:
        
        accomodation_by_id = firebase_config.db.child("accommodation").child(accommodation_id).get().val()
       
        if accomodation_by_id is None:
            raise HTTPException(status_code=404, detail="Accommodation not found.")
        
        firebase_config.db.child("accommodation").child(accommodation_id).remove()
        return "Accommodation deleted successfully!"
    except Exception:
         raise HTTPException(status_code=400, detail= "Erro ao deletar acomodação de id:{accomodation_id}")
    
