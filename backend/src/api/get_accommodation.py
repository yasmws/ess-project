
from fastapi import HTTPException
import src.db.firebase_config as firebase_config

storage = firebase_config.firebase.storage()

def get_accommodations(id_client):
    
    result = []
    try:
        reservation_node = firebase_config.db.child("accommodation").get().val()

        for _, info in reservation_node.items():
            if info['user_id'] == id_client:
                image_url = storage.child("accommodation").child("be7cf4d8-f408-41e7-85f2-920b5be751c4").get_url(None)
                obj = {'name': info['name'], 'location': info['location'], 'description': info['description'], 'id': info['id'], 'img_url': image_url}
                result.append(obj)
        
        return HTTPException(status_code=200, detail=result)
        
    except Exception:
        raise HTTPException(status_code=400, detail="Erro interno do servidor")
    
