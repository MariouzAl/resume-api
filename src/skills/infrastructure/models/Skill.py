from datetime import date
import uuid
from sqlmodel import Field, Relationship, SQLModel

from src.project.infrastructure.models.project import Project
from src.project.infrastructure.models.project_techstack_link import ProjectTechStackLink



class Skill(SQLModel, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    skill: str
    level: int
    firstUsedDate: date
    
    #professional_experiences:list['ProfessionalExperience']=Relationship(back_populates='tech_stack', link_model=ProfessionalExperienceSkillLink)
    projects :list[Project]=Relationship(back_populates='skills', link_model=ProjectTechStackLink)