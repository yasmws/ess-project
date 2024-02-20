from fastapi import HTTPException
from  src.db import firebase_config
from src.service.validation import Validation

def check_any_reservation(accommodation_id):
        
        reservations = firebase_config.db.child("accommodation").child(accommodation_id).child("reservations")

        reservations = reservations.get().val()
        
        for _, info in reservations.items():
            
            disponibilidade = info['disponibility']
            
            if not disponibilidade:
                 return True #existe reserva
        
        return False   #nao existe reserva
        
def delet_accommodation(accommodation_id):

    # validação
    ## ver se id de acomodação existe
    if Validation.get_accommodation_by_id(accommodation_id) is None:   
         raise HTTPException(status_code=404, detail="A acomodação não existe")
    
    valid = check_any_reservation(accommodation_id)
    ## ver se id de acomodação não tem acomodação
    if valid:
        raise HTTPException(status_code=400, detail="Não se pode deletar acomodações com reservas")
        #return "Can't delet an accommodation with reservations"
    try:
        firebase_config.db.child("accommodation").child(accommodation_id).remove()
        raise HTTPException(status_code=200, detail= "Acomodação deleta com sucesso")
    except Exception:
         raise HTTPException(status_code=400, detail= "Erro ao deletar acomodação de id:{accomodation_id}")
    