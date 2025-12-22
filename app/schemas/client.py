from pydantic import BaseModel
import datetime

class Client(BaseModel):
    id: int = -1
    fio: str
    email_client: str
    date_registration_client: datetime.datetime


