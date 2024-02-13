from fastapi import HTTPException
import firebase_config as firebase_config


def update_accommodation(accommodation_id, accommodation_name=None, accommodation_loc=None, 
                         accommodation_bedrooms=None, accommodation_max_capacity=None, 
                         accommodation_description=None):
    
    try:
        current_data = firebase_config.db.child("accommodation").child(accommodation_id).get().val()
       
        
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

    
