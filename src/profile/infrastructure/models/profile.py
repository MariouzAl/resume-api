
from datetime import date
import uuid
from sqlmodel import SQLModel,Field


class Profile(SQLModel, table=True ):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    birthday: date
    phone: str
    city: str
    email: str
    freelance: str
    degree: str
    description: str
    