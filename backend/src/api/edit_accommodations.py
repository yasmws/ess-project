from fastapi import HTTPException
from  src.db import firebase_config
from src.api.delete_accommodations import check_any_reservation

#------------ ver se accomodation existe

## validar e editar imagem
def update_accommodation(accommodation_id, accommodation_name, accommodation_loc, 
                         accommodation_bedrooms, accommodation_max_capacity, 
                         accommodation_description):
    # tem ou não reservas
    valid = check_any_reservation(accommodation_id)
    current_data = firebase_config.db.child("accommodation").child(accommodation_id).get().val()

    if valid[1]:

        if not valid[0]:
            # O retorno falso, significa que existe reserva. Apenas será editado a descrição
            # e capacidade máxima caso seja maior do que anterior

            if  accommodation_name or accommodation_loc or accommodation_bedrooms :
                return "Exist fields that are not editable"
            
            if accommodation_description is not None:
                firebase_config.db.child("accommodation").child(accommodation_id).update({'description': accommodation_description})

            if accommodation_max_capacity is not None and current_data['max_capacity'] <= accommodation_max_capacity:
                firebase_config.db.child("accommodation").child(accommodation_id).update({'max_capacity': accommodation_max_capacity})
            elif current_data['max_capacity'] > accommodation_max_capacity:
                return "Invalid max capacity value"
            return ("Accommodation updated successfully!")
        try:
        
            if current_data is None:
                raise HTTPException(status_code=404, detail="Accommodation not found.")

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

            return ("Accommodation updated successfully!")
        except Exception:
            raise HTTPException(status_code=400, detail="Failed to update accommodation.")
        
    raise HTTPException(status_code=404, detail="The accomodation not exist")
        
