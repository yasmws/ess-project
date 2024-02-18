from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class ItemModel(BaseModel):
    id= str,
    checkin_date= str,
    checkout_date= str,
    accommodation_id= str,
    cliente_id= str