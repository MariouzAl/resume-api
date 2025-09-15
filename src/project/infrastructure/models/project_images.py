

from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel
if TYPE_CHECKING:
    from src.project.infrastructure.models.project import Project


class ProjectImages(SQLModel, table=True):
    id :UUID|None = Field(primary_key=True, default_factory=uuid4)
    url : str
    project_id : UUID|None = Field(foreign_key='project.id',default=None,ondelete='CASCADE')
    
    project:'Project'= Relationship(back_populates='images')
    
    