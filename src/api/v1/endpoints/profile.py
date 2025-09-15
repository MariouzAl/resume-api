from datetime import date
from uuid import UUID

from pydantic import BaseModel
from sqlmodel import Session
from src.core.database import get_session

from fastapi import APIRouter, Depends

from src.profile.application.use_cases import GetProfileById, GetProfiles,UpdateProfile,CreateProfile
from src.profile.application.use_cases.create_profile import CreateProfileParams
from src.profile.application.use_cases.get_profile_by_id import GetProfileParms
from src.profile.application.use_cases.update_profile import UpdateProfileParams
from src.profile.domain.entitites.profile_entity import ProfileEntity
from src.profile.infrastructure.repositories import (
    SQLModelProfileRepository as ProfileRepository,
)


class ProfileBody(BaseModel):
    name: str
    birthday: date
    phone: str
    city: str
    email: str
    freelance: str
    degree: str
    description: str

router = APIRouter()
router.prefix ='/bio'

@router.get("/")
def get_list_of_profiles( session: Session = Depends(get_session)):
    repository = ProfileRepository(session)
    profile = GetProfiles(repository).execute()

    return profile

@router.get("/{id}")
def get_profile_info(id: UUID, session: Session = Depends(get_session)):
    repository = ProfileRepository(session)
    profile = GetProfileById(repository).execute(GetProfileParms(id=id))
    return profile


@router.put("/{id}")
def update_profile(id: UUID, body:ProfileBody, session: Session = Depends(get_session)):
    updated_profile=ProfileEntity(id=id,
                            **body.model_dump()
            )
    repository = ProfileRepository(session)
    profile = UpdateProfile(repository).execute(UpdateProfileParams(updated_profile))
    return profile


@router.post("/")
def create_profile(body:ProfileBody, session: Session = Depends(get_session)):
    profile=ProfileEntity(**body.model_dump())  
    repository = ProfileRepository(session)
    profile = CreateProfile(repository).execute(CreateProfileParams(profile))
    return profile


