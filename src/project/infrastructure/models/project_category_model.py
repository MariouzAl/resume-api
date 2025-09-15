from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel
from src.project.infrastructure.models.project_category_link import ProjectCategoryLink

if TYPE_CHECKING:
    from .project import Project

class ProjectCategory(SQLModel, table=True):
    __tablename__ = "project_category" # type: ignore
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
    name: str
    
    projects:list["Project"]= Relationship(
        back_populates="categories",
        link_model=ProjectCategoryLink
    )


