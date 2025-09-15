from datetime import date
from uuid import UUID

from pydantic import BaseModel
from sqlmodel import Session
from src.core.database import get_session

from fastapi import APIRouter, Depends

from src.education.application.use_cases import CreateEducation,GetEducationList
from src.education.application.use_cases.create_education import CreateEducationParams
from src.education.application.use_cases.get_education_by_id import GetEducationById, GetEducationByIdParams
from src.education.domain.entities.education_entity import EducationEntity
from src.education.infrastructure.repositories.sqlmodel_education_repository import (
    SQLModelEducationRepository,
)


class EducationBody(BaseModel):
    title:str
    dateStart:date
    dateFinished :date
    institute:str
    description:str
    user_id:UUID

router = APIRouter()
router.prefix ='/education'

@router.post("/")
def create_education(body:EducationBody, session: Session = Depends(get_session)):
    repository = SQLModelEducationRepository(session)
    entity=EducationEntity(**body.model_dump())  
    education = CreateEducation(repository).execute(CreateEducationParams(entity))
    print(education)
    return education

@router.get("/")
def get_list_of_educations( session: Session = Depends(get_session)):
    repository = SQLModelEducationRepository(session)
    education_list = GetEducationList(repository).execute()
    return education_list

@router.get("/{id}")
def get_education_info(id: UUID, session: Session = Depends(get_session)):
    repository = SQLModelEducationRepository(session)
    education_item = GetEducationById(repository).execute(GetEducationByIdParams(id=id))
    return education_item
""" 



@router.put("/{id}")
def update_education(id: UUID, body:educationBody, session: Session = Depends(get_session)):
    updated_education=educationEntity(id=id,
                            **body.model_dump()
            )
    repository = educationRepository(session)
    education = Updateeducation(repository).execute(UpdateeducationParams(updated_education))
    return education
 """
