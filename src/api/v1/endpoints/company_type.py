from http import client
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.core.database import get_session
from src.professional_experience.application.use_cases import (
    GetAllCompanies,
    RegisterCompany,
    GetCompanyById,
    DeleteCompany
)
from src.professional_experience.application.use_cases.register_company import (
    RegisterCompanyParams,
)
from src.professional_experience.domain.entities.company import Company
from src.professional_experience.domain.repositories.base_company_repository import (
    BaseCompanyRepository,
)
from src.professional_experience.domain.repositories.base_company_type_repository import BaseCompanyTypeRepository
from src.professional_experience.infrastructure.repositories.sqlmodel_company_repository import (
    SQLModelCompanyRepository,
)
from src.professional_experience.infrastructure.repositories.sqlmodel_company_type_repository import SQLModelCompanyTypeRepository


router = APIRouter()
router.prefix = "/company-type"


class CreateCompanyTypeBodyParams(BaseModel):
    name: str


class CompanyTypeResponse(BaseModel):
    id: UUID
    name: str


@router.post("/")
def add_a_company_type(
    body: CreateCompanyTypeBodyParams, session=Depends(get_session)
) -> CompanyTypeResponse:
    repository: BaseCompanyTypeRepository = SQLModelCompanyTypeRepository(session)
    item: Company | None = RegisterCompany(repository).execute(
        RegisterCompanyParams(**body.model_dump())
    )
    if not item:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    if not item.id:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    return CompanyTypeResponse(id=item.id, name=item.name)


@router.get("/")
def get_company_list(
    session=Depends(get_session),
) -> list[CompanyTypeResponse]:
    repository: BaseCompanyRepository = SQLModelCompanyRepository(session)

    companies = GetAllCompanies(repository).execute()
    if not companies:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    response = [
        CompanyTypeResponse(name=company.name, id=company.id)
        for company in companies
        if company.id is not None
    ]
    return response


def get_existing_company(id: UUID, session=Depends(get_session)) -> Company:
    repository = SQLModelCompanyRepository(session)
    find_skill_by_id = GetCompanyById(repository)
    skill = find_skill_by_id.execute(id=id)

    if skill is None:
        raise HTTPException(status_code=client.NOT_FOUND, detail="Skill not found")
    return skill


@router.get("/{id}", response_model=CompanyTypeResponse)
def get_skill_by_id(
    company: Company = Depends(get_existing_company),
) -> CompanyTypeResponse:
    if not company.id:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    return CompanyTypeResponse(id=company.id, name=company.name)


@router.delete("/{id}")
def delete_skill_by_id(company: Company = Depends(get_existing_company), session=Depends(get_session)):
    # La habilidad ya está disponible aquí, no hay necesidad de buscarla de nuevo
    repository = SQLModelCompanyRepository(session)
    delete_skill = DeleteCompany(repository)
    if not company.id:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    deleted_skill = delete_skill.execute(company.id)
    return deleted_skill