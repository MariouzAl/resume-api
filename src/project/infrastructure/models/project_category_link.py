from uuid import UUID
from sqlmodel import Field, SQLModel


class ProjectCategoryLink(SQLModel, table=True):
    project_id: UUID | None = Field(
        default=None, foreign_key="project.id", primary_key=True
    )
    category_id: UUID | None = Field(
        default=None, foreign_key="project_category.id", primary_key=True
    )
