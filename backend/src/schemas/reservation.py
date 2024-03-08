from datetime import date
from pydantic import BaseModel, validator

class Reservation(BaseModel):
    id: str
    #checkin_date: date
    #checkout_date: date
    accommodation_id: str
    client_id: str

    def __init__(self, id, accommodation_id, client_id):
        self.id = id
        self.accommodation_id = accommodation_id
        self.client_id = client_id
        
