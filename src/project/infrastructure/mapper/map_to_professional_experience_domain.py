# Archivo: src/infrastructure/mappers.py

from src.professional_experience.domain.entities import ProfessionalExperience as ProfessionalExperienceDomain
from src.professional_experience.domain.entities.company import Company
from src.professional_experience.domain.entities.company_type import CompanyType
from src.professional_experience.infrastructure.models import ProfessionalExperience as ProfessionalExperienceSQLModel
from src.project.infrastructure.mapper import map_to_project
from src.skills.domain.entities.skill_entity import Skill as SkillDomain
from src.skills.infrastructure.models.Skill import Skill as SkillModel


def map_to_skill_domain(model:SkillModel) -> SkillDomain|None:
    if model is None :
        return None
    if model.id is None:
        return None
        
    return SkillDomain(
        id=model.id,
        skill= model.skill,
        firstUsedDate=model.firstUsedDate,
        level=model.level
    )


def map_to_professional_experience_domain(
    pe_model: ProfessionalExperienceSQLModel
) -> ProfessionalExperienceDomain:
    """
    Convierte un ProfessionalExperienceSQLModel a una entidad de dominio ProfessionalExperience.
    """
    if pe_model is None:
        return None

    # Extracción de IDs de tecnologías y descripciones de responsabilidades
    company:Company = Company(id=pe_model.company.id, name =pe_model.company.name,company_type=CompanyType(
            id=pe_model.company.company_type.id, name=pe_model.company.company_type.name
        ),)

    if pe_model.id is None or pe_model.company_id is None:
        raise ValueError("ProfessionalExperience must have an ID and company_id to be a valid domain entity.")


    return ProfessionalExperienceDomain(
        id=pe_model.id,
        key=pe_model.key,
        company_id=pe_model.company_id,
        company=company,
        startDate=pe_model.startDate,
        endDate=pe_model.endDate,
        position=pe_model.position,
        projects=[map_to_project(project) for project in (pe_model.projects if pe_model.projects is not None else []) ]
    )