from pydantic import BaseModel
from typing import List, Optional

class ClubIn(BaseModel):
    name: str
    phone: str
    count_users: str
    country: str


class ClubOut(ClubIn):
    id: int
