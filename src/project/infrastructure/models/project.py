from typing import TYPE_CHECKING
from datetime import date
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel
from src.professional_experience.infrastructure.models.professional_experience_model import CompanyType, ProfessionalExperience
from src.project.infrastructure.models.project_category_link import ProjectCategoryLink
from src.project.infrastructure.models.project_techstack_link import (
    ProjectTechStackLink,
)


if TYPE_CHECKING:
    from src.professional_experience.infrastructure.models.professional_experience_model import Responsibility
    from src.project.infrastructure.models.project_images import ProjectImages
    from src.project.infrastructure.models import ProjectCategory
    from src.skills.infrastructure.models import Skill


class Project(SQLModel, table=True):
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
    project: str
    shortDescription: str
    fullDescription: str
    link: str
    projectLink: str
    cover: str
    key: str= Field(unique=True)
    start_date: date
    end_date: date
    skills: list["Skill"] = Relationship(
        back_populates="projects", link_model=ProjectTechStackLink
    )

    images: list["ProjectImages"] = Relationship(back_populates="project")
    categories: list["ProjectCategory"]|None = Relationship(
        back_populates="projects", link_model=ProjectCategoryLink
    )
    responsibilities : list['Responsibility'] = Relationship(back_populates='project')
    professional_experience_id : UUID | None = Field(default=None, foreign_key="professional_experience.id")
    professional_experience :ProfessionalExperience|None = Relationship(back_populates='projects')
    
    project_company_type_id:UUID|None=  Field(default=None, foreign_key="company_type.id")
    project_company_type: "CompanyType"= Relationship()
    
