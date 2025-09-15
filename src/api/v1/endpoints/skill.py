from datetime import date
from http import client
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.skills.application.use_cases import (
    GetAllSkills,
    FindSkillById,
    CreateSkill,
    DeleteSkill,
)
from src.core.database import get_session
from src.skills.application.use_cases.create_skill import CreateSkillParams
from src.skills.application.use_cases.delete_skill import DeleteSkillParams
from src.skills.application.use_cases.find_skill_by_id import FindSkillByIdParams
from src.skills.domain.entities.skill_entity import Skill
from src.skills.infrastructure.repositories.sqlmodel_skill_repository import (
    SkillRepository,
)

router = APIRouter()
router.prefix="/skill"

class CreateSkillBodyParams(BaseModel):
    skill: str
    level: int
    firstUsedDate: date


class SkillResponse(BaseModel):
    id: UUID
    skill: str
    level: int
    firstUsedDate: date


@router.get("/")
def get_skill(session=Depends(get_session)) -> list[SkillResponse]:
    repository: SkillRepository = SkillRepository(session)
    get_all_skills_use_case = GetAllSkills(repository)
    skills = get_all_skills_use_case.execute()
    response = [
        SkillResponse(
            id=skill.id,
            level=skill.level,
            skill=skill.skill,
            firstUsedDate=skill.firstUsedDate,
        )
        for skill in skills
        if skill.id is not None
    ]
    return response


def get_existing_skill(id: UUID, session=Depends(get_session)) -> Skill:
    """
    Dependencia que busca una habilidad por su ID.
    Si no la encuentra, lanza un error HTTP 404 automáticamente.
    """
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
    if skill.id is None:
        raise HTTPException(404)
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





@router.post("/")
def create_skill(
    body: CreateSkillBodyParams, session=Depends(get_session)
) -> SkillResponse:
    repository: SkillRepository = SkillRepository(session)
    create_skill = CreateSkill(repository)
    skill = create_skill.execute(CreateSkillParams(**body.model_dump()))
    if not skill:
         raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    return SkillResponse(**skill.dict())
