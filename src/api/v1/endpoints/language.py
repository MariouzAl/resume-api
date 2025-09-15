from http import client
from typing import Literal
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.language.application.use_cases import AddLanguage, GetAllLanguages
from src.core.database import get_session
from src.language.domain.entities.language_entity import Language
from src.language.infrastructure.repositories.sqlmodel_language_repository import (
    SQLLanguageRepository,
)

router = APIRouter()
router.prefix = "/language"


class AddLangugageBodyParams(BaseModel):
    language: str
    level: Literal["Basic", "Fluent", "Advanced", "Native"]


class LanguageResponse(BaseModel):
    id: UUID
    language: str
    level: str


@router.get("/")
def get_all_language(session=Depends(get_session)) -> list[LanguageResponse]:
    repository: SQLLanguageRepository = SQLLanguageRepository(session)
    get_all_skills_use_case = GetAllLanguages(repository)
    language = get_all_skills_use_case.execute()
    response = [
        LanguageResponse(
            id=skill.id,
            level=skill.level,
            language=skill.language,
        )
        for skill in language
        if skill.id is not None
    ]
    return response


@router.post("/")
def add_language(
    body: AddLangugageBodyParams, session=Depends(get_session)
) -> LanguageResponse:
    repository: SQLLanguageRepository = SQLLanguageRepository(session)
    add_language = AddLanguage(repository)
    language = add_language.execute(Language(**body.model_dump()))
    if not language:
        raise HTTPException(
            status_code=client.INTERNAL_SERVER_ERROR,
        )
    return LanguageResponse(**language.dict())
