from datetime import date
import uuid
from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.project.infrastructure.models.project import Project



class CompanyType (SQLModel, table=True):
    __tablename__ = "company_type"  # type: ignore
    id: uuid.UUID | None = Field(primary_key=True, default_factory=uuid.uuid4)
    name:str
    companies : list['Company']|None = Relationship(back_populates='company_type')


class Company(SQLModel, table=True):
    id: uuid.UUID | None = Field(primary_key=True, default_factory=uuid.uuid4)
    name: str
    professional_experiences: list["ProfessionalExperience"] = Relationship(
        back_populates="company"
    )
    company_type_id:uuid.UUID = Field(foreign_key='company_type.id',nullable=True,default=None, ondelete="SET NULL")
    company_type:CompanyType = Relationship(back_populates="companies")

class ProfessionalExperience(SQLModel, table=True):
    __tablename__ = "professional_experience"  # type: ignore
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    key: str
    startDate: date
    endDate: date
    position: str
    company_id: uuid.UUID  = Field(
        foreign_key="company.id", nullable=True, default=None
    )
    company: Company = Relationship(back_populates="professional_experiences")
    projects : list['Project']|None = Relationship(back_populates='professional_experience')


class Responsibility(SQLModel, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    description: str
    project_id: uuid.UUID | None = Field(default=None, foreign_key="project.id", ondelete="CASCADE")
    project: "Project" = Relationship(back_populates="responsibilities")
