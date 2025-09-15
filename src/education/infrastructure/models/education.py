
from datetime import date
import uuid
from sqlmodel import SQLModel, Field

class Education(SQLModel,table=True) :
        id: uuid.UUID | None=Field(default_factory=uuid.uuid4,  primary_key=True)
        title: str
        dateStart: date
        dateFinished: date|None 
        institute: str 
        description: str 
        user_id:uuid.UUID|None =Field(foreign_key='profile.id',default=None)