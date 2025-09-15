from http import client
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.core.database import get_session
from src.project.application.use_cases import CreateProjectCategory, GetAllProjectCategory,GetProjectCategoryById

from src.project.application.use_cases.create_project_category import (
    CreateProjectCategoryParams
)
from src.project.domain.entities.project_category import ProjectCategory
from src.project.domain.repositories.base_project_category_repository import (
    BaseProjectCategoryRepository,
)
from src.project.infrastructure.repositories.sqlmodel_project_category_repository import (
    SQLModelProjectCategoryRepository,
)


router = APIRouter()
router.prefix = "/project-category"


class CreateProjectCategoryBodyParams(BaseModel):
    name: str


class ProjectCategoryResponse(BaseModel):
    id: UUID
    name: str


@router.post("/")
def add_a_project_category(
    body: CreateProjectCategoryBodyParams, session=Depends(get_session)
) -> ProjectCategoryResponse:
    repository: BaseProjectCategoryRepository = SQLModelProjectCategoryRepository(
        session
    )
    item: ProjectCategory | None = CreateProjectCategory(repository).execute(
        CreateProjectCategoryParams(name=body.name)
    )
    if not item:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    if not item.id:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    return ProjectCategoryResponse(id=item.id, name=item.name)


@router.get("/")
def get_project_category_list(
    session=Depends(get_session),
) -> list[ProjectCategoryResponse]:
    repository: BaseProjectCategoryRepository = SQLModelProjectCategoryRepository(session)

    project_categories = GetAllProjectCategory(repository).execute()
    if not project_categories:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    response = [
        ProjectCategoryResponse(name=project_category.name, id=project_category.id)
        for project_category in project_categories
        if project_category.id is not None
    ]
    return response


def get_existing_project_category(id: UUID, session=Depends(get_session)) -> ProjectCategory:
    repository = SQLModelProjectCategoryRepository(session)
    find_project_category = GetProjectCategoryById(repository)
    project_category = find_project_category.execute(id=id)
    if project_category is None:
        raise HTTPException(status_code=client.NOT_FOUND, detail="project category not found")
    return project_category

@router.get("/{id}", response_model=ProjectCategoryResponse)
def get_skill_by_id(
    project_category: ProjectCategory = Depends(get_existing_project_category),
) -> ProjectCategoryResponse:
    if not project_category.id:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    return ProjectCategoryResponse(id=project_category.id, name=project_category.name)

""" 







@router.delete("/{id}")
def delete_skill_by_id(project_category: ProjectCategory = Depends(get_existing_project_category), session=Depends(get_session)):
    # La habilidad ya está disponible aquí, no hay necesidad de buscarla de nuevo
    repository = SQLModelProjectCategoryRepository(session)
    delete_skill = DeleteProjectCategory(repository)
    if not project_category.id:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    deleted_skill = delete_skill.execute(project_category.id)
    return deleted_skill """
