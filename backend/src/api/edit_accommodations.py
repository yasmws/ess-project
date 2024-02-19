from fastapi import HTTPException
from  src.db import firebase_config
from src.api.delete_accommodations import check_any_reservation
from src.service.validation import Validation

#------------ ver se accomodation existe

## validar e editar imagem
def update_accommodation(accommodation_id, accommodation_name, accommodation_loc, 
                         accommodation_bedrooms, accommodation_max_capacity, 
                         accommodation_description):
    # tem ou não reservas

    current_data = Validation.get_accommodation_by_id(accommodation_id)

    if current_data:
        valid = check_any_reservation(accommodation_id)

    else:
        return HTTPException(status_code=404, detail="Acomodação não encontrada")

    if valid:
        # O retorno falso, significa que existe reserva. Apenas será editado a descrição
        # e capacidade máxima caso seja maior do que anterior
        if  accommodation_name or accommodation_loc or accommodation_bedrooms :
                raise HTTPException(status_code=400, detail= "Campos inválidos")
        
        if accommodation_description is not None:
            firebase_config.db.child("accommodation").child(accommodation_id).update({'description': accommodation_description})

        if accommodation_max_capacity is not None and current_data['max_capacity'] <= accommodation_max_capacity:
            firebase_config.db.child("accommodation").child(accommodation_id).update({'max_capacity': accommodation_max_capacity})
        elif current_data['max_capacity'] > accommodation_max_capacity:
                raise HTTPException(status_code=400, detail="Invalid max capacity value")
        
        raise HTTPException(status_code=200, detail="Acomodação editada com sucesso!")

    else :
        try:

            update_data = {
                "name": current_data["name"],
                "location": current_data["location"],
                "bedrooms": current_data["bedrooms"],
                "max_capacity": current_data["max_capacity"],
                "description": current_data["description"],
            }

            if accommodation_name is not None:
                update_data["name"] = accommodation_name
            if accommodation_loc is not None:
                update_data["location"] = accommodation_loc
            if accommodation_bedrooms is not None:
                update_data["bedrooms"] = accommodation_bedrooms
            if accommodation_max_capacity is not None:
                update_data["max_capacity"] = accommodation_max_capacity
            if accommodation_description is not None:
                update_data["description"] = accommodation_description

            firebase_config.db.child("accommodation").child(accommodation_id).update(update_data)

            return HTTPException(status_code=200, detail="Acomodação editada com sucesso!")
        
        except Exception:
            raise HTTPException(status_code=400, detail="Falha em atualizar acomodação")

        
