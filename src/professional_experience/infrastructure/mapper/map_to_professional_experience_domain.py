# Archivo: src/infrastructure/mappers.py

from src.professional_experience.domain.entities import (
    ProfessionalExperience as ProfessionalExperienceDomain,
)
from src.professional_experience.domain.entities.company import Company
from src.professional_experience.domain.entities.company_type import CompanyType
from src.professional_experience.infrastructure.models import (
    ProfessionalExperience as ProfessionalExperienceSQLModel,
)
from src.project.domain.entities.project import Project
from src.project.infrastructure.mapper.map_to_project import map_to_project
from src.skills.domain.entities.skill_entity import Skill as SkillDomain
from src.skills.infrastructure.models.Skill import Skill as SkillModel


def map_to_skill_domain(model: SkillModel) -> SkillDomain | None:
    if model is None:
        return None
    if model.id is None:
        return None

    return SkillDomain(
        id=model.id,
        skill=model.skill,
        firstUsedDate=model.firstUsedDate,
        level=model.level,
    )


def map_to_professional_experience_domain(
    model: ProfessionalExperienceSQLModel,
) -> ProfessionalExperienceDomain:
    """
    Convierte un ProfessionalExperienceSQLModel a una entidad de dominio ProfessionalExperience.
    """
    if model is None:
        return None
    
    if model.company.company_type is None:
        model.company.company_type

    company: Company = Company(
        id=model.company.id,
        name=model.company.name,
        company_type=CompanyType(
            id=model.company.company_type.id, name=model.company.company_type.name
        ),
    )
    projects_result = model.projects if model.projects is not None else []
    projects_result = sorted(
    projects_result,
    key=lambda p: (p.start_date, p.end_date),
    reverse=True
)
    projects: list[Project] = [map_to_project(project) for project in projects_result]
    return ProfessionalExperienceDomain(
        id=model.id,
        key=model.key,
        company_id=model.company_id,
        company=company,
        startDate=model.startDate,
        endDate=model.endDate,
        position=model.position,
        projects=projects,
    )
