from fastapi import HTTPException
import firebase_config as firebase_config


def check_any_reservation(accommodation_id):
        
        reservations =  firebase_config.db.child("accommodation").child(accommodation_id)

        if reservations.get().val() is not None:
             exist = True
        else:
            exist = False
        
        reservations = firebase_config.db.child("accommodation").child(accommodation_id).child("reservations")

        reservations = reservations.get().val()
        
        for _, info in reservations.items():
            
            disponibilidade = info['disponibility']
            if not disponibilidade:
                 return [False, exist]
        
        return [True, exist]
        


def delet_accommodation(accommodation_id):

    ## passou no teste de ter acomodações
   
    # validação
    valid = check_any_reservation(accommodation_id)

    ## ver se id de acomodação existe
    if not valid[1]:
         raise HTTPException(status_code=404, detail="The accomodation not exist")
    
    ## ver se id de acomodação não tem acomodação
    if not valid[0]:
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
    
