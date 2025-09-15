import uuid
from sqlmodel import Field, SQLModel




class Language(SQLModel, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    language: str
    level: str