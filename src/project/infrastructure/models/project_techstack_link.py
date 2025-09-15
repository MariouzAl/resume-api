from uuid import UUID
from sqlmodel import Field, SQLModel


class ProjectTechStackLink(SQLModel, table=True):
    project_id: UUID | None = Field(
        default=None, foreign_key="project.id", primary_key=True
    )
    skill: UUID | None = Field(
        default=None, foreign_key="skill.id", primary_key=True
    )
