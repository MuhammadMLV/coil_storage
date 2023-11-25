from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CoilModel(BaseModel):
    id: int
    length: float
    weight: float
    date_add: datetime = datetime.now()
    date_remove: Optional[datetime] = None
