from uuid import UUID

from pydantic import BaseModel
from sqlmodel import Session
from src.core.database import get_session

from fastapi import APIRouter, Depends

from src.tech_profile.application.use_cases import GetProfileById, GetTechProfiles,UpdateProfile,CreateProfile
from src.tech_profile.application.use_cases.create_tech_profile import CreateProfileParams
from src.tech_profile.application.use_cases.get_tech_profile_by_id import GetProfileParms
from src.tech_profile.application.use_cases.update_tech_profile import UpdateProfileParams
from src.tech_profile.domain.entitites.tech_profile_entity import TechProfileEntity
from src.tech_profile.infrastructure.repositories import (
    SQLModelTechProfileRepository as ProfileRepository,
)

    
class TechProfileBody(BaseModel):
    description: str
    focus:str

router = APIRouter()
router.prefix ='/tech-profile'

@router.get("/")
def get_list_of_profiles( session: Session = Depends(get_session)):
    repository = ProfileRepository(session)
    profile = GetTechProfiles(repository).execute()

    return profile

@router.get("/{id}")
def get_profile_info(id: UUID, session: Session = Depends(get_session)):
    repository = ProfileRepository(session)
    profile = GetProfileById(repository).execute(GetProfileParms(id=id))
    return profile


@router.put("/{id}")
def update_profile(id: UUID, body:TechProfileBody, session: Session = Depends(get_session)):
    updated_profile=TechProfileEntity(id=id,
                            **body.model_dump()
            )
    repository = ProfileRepository(session)
    profile = UpdateProfile(repository).execute(UpdateProfileParams(updated_profile))
    return profile


@router.post("/")
def create_profile(body:TechProfileBody, session: Session = Depends(get_session)):
    profile=TechProfileEntity(focus=body.focus, description=body.description)  
    repository = ProfileRepository(session)
    profile = CreateProfile(repository).execute(CreateProfileParams(profile))
    return profile


