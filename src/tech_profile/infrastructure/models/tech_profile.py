import uuid
from sqlmodel import SQLModel, Field


class TechProfile(SQLModel, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    focus: str = Field(index=True,default='FullStack')
    description: str
