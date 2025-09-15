from datetime import date
from http import client
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.core.database import get_session
from src.professional_experience.application.use_cases.create_professional_experience import (
    CreateProfessionalExperienceParams,
)
from src.professional_experience.application.use_cases.get_all_professional_experience import (
    GetAllProfessionalExperience,
)
from src.professional_experience.domain.entities.professional_experience import (
    ProfessionalExperience,
)
from src.professional_experience.domain.repositories.base_professional_experience_repository import (
    BaseProfessionalExperienceRepository,
)
from src.professional_experience.infrastructure.repositories.sqlmodel_professional_experience_repository import (
    SQLModelProfessionalExperienceRepository,
)
from src.professional_experience.application.use_cases import (
    CreateProfessionalExperience,
)

router = APIRouter()
router.prefix = "/professional-experience"


class CreateProfessionalExperienceBodyParams(BaseModel):
    key: str
    company_id: UUID
    startDate: date
    endDate: date
    technologies: list[UUID]
    responsibilities: list[str]
    position: str


class CompanyResponse(BaseModel):
    id: UUID
    name: str


class SkillResponse(BaseModel):
    id: UUID
    name: str


class ProfessionalExperienceResponse(BaseModel):
    id: UUID
    company : CompanyResponse
    key: str
    startDate: date
    endDate: date
    position: str
    responsibilities: list[str]|None=None
    tech_stack : list[SkillResponse]|None=None


@router.post("/")
def add_a_professional_experience(
    body: CreateProfessionalExperienceBodyParams, session=Depends(get_session)
) -> ProfessionalExperienceResponse:
    repository: BaseProfessionalExperienceRepository = (
        SQLModelProfessionalExperienceRepository(session)
    )
    item: ProfessionalExperience | None = CreateProfessionalExperience(
        repository
    ).execute(CreateProfessionalExperienceParams(**body.model_dump()))
    if not item:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    return ProfessionalExperienceResponse(**item.dict())


@router.get("/")
def get_professional_experience_list(
    session=Depends(get_session),
) -> list[ProfessionalExperienceResponse]:
    repository: BaseProfessionalExperienceRepository = (
        SQLModelProfessionalExperienceRepository(session)
    )
    get_all_skills_use_case = GetAllProfessionalExperience(repository)
    professional_experiences = get_all_skills_use_case.execute()
    if not professional_experiences:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    print("PROFESSIONAL EXPERIENCES", [pe.dict() for pe in professional_experiences])
    response = [
    ProfessionalExperienceResponse(
        id=item.id,
        company=CompanyResponse(id=company_id, name=item.company.name),
        endDate=item.endDate,
        key=item.key,
        position=item.position,
        startDate=item.startDate
    )
    for item in professional_experiences
    if item.id is not None
    if (company_id := item.company.id) is not None # <-- Revisa y asigna el company_id
    ]
    return response


""" 

def get_existing_skill(id: UUID, session=Depends(get_session)) -> Skill:
    repository = SkillRepository(session)
    find_skill_by_id = FindSkillById(repository)
    skill = find_skill_by_id.execute(FindSkillByIdParams(id=id))

    if skill is None:
        raise HTTPException(
            status_code=client.NOT_FOUND,
            detail="Skill not found"
        )
    return skill

# PASO 2: Usa la dependencia en tus rutas
@router.get("/{id}", response_model=SkillResponse)
def get_skill_by_id(skill: Skill = Depends(get_existing_skill)) -> SkillResponse:
    # La habilidad ya fue encontrada y el 404 ya fue manejado por la dependencia
    return SkillResponse(
        id=skill.id,
        level=skill.level,
        skill=skill.skill,
        firstUsedDate=skill.firstUsedDate,
    )


@router.delete("/{id}")
def delete_skill_by_id(skill: Skill = Depends(get_existing_skill), session=Depends(get_session)):
    # La habilidad ya está disponible aquí, no hay necesidad de buscarla de nuevo
    repository = SkillRepository(session)
    delete_skill = DeleteSkill(repository)
    deleted_skill = delete_skill.execute(DeleteSkillParams(id=skill.id))
    return deleted_skill


 """
