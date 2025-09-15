from datetime import date
from http import client
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.core.database import get_session
from src.project.application.use_cases.create_project import (
    CreateProjectParams,
)
from src.project.application.use_cases import (
    GetAllProjects,
)
from src.project.domain.entities.project import (
    Project,
)
from src.project.domain.repositories.base_project_repository import (
    BaseProjectRepository,
)
from src.project.infrastructure.repositories.sqlmodel_project_repository import (
    SQLModelProjectRepository,
)
from src.project.application.use_cases import (
    CreateProject,
)

router = APIRouter()
router.prefix = "/project"


class CreateProjectBodyParams(BaseModel):
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

class ProjectCategoryResponse(BaseModel):
    id:UUID
    name:str

class ProjectResponse(BaseModel):
    id: UUID|None
    project: str
    shortDescription: str
    fullDescription: str
    link: str
    projectLink: str
    categories: list[ProjectCategoryResponse]
    cover: str
    builtWith: list[str]
    images: list[str]
    key: str
    start_date:date
    end_date:date
    


@router.post("/")
def add_a_project(
    body: CreateProjectBodyParams, session=Depends(get_session)
) -> ProjectResponse:
    repository: BaseProjectRepository = (
        SQLModelProjectRepository(session)
    )
    item: Project | None = CreateProject(
        repository
    ).execute(CreateProjectParams(**body.model_dump()))
    if not item:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    return ProjectResponse(**item.dict())


@router.get("/")
def get_project_list(
    session=Depends(get_session),
) -> list[ProjectResponse]:
    repository: BaseProjectRepository = (
        SQLModelProjectRepository(session)
    )
    get_all_projects_use_case = GetAllProjects(repository)
    projects = get_all_projects_use_case.execute()
    if not projects:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    response = [
    ProjectResponse(
        id= item.id,
        project= item.project,
        shortDescription= item.shortDescription,
        link= item.link,
        projectLink= item.projectLink,
        categories=[ProjectCategoryResponse(id=cat_id, name=cat.name  ) for cat in item.categories if (cat_id := cat.id) is not None ],
        cover= item.cover,
        builtWith=item.builtWith,
        images=item.images,
        key= item.key,
        start_date=item.start_date,
        end_date=item.end_date,
        fullDescription=item.fullDescription
    )
    for item in projects
    if item.id is not None
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
