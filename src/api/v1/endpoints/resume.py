from enum import Enum
from http.client import INTERNAL_SERVER_ERROR
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query, Response

from src.core.database import get_session
from src.education.application.use_cases.get_education_list import GetEducationList
from src.education.infrastructure.repositories.sqlmodel_education_repository import SQLModelEducationRepository
from src.language.application.use_cases.get_all_language import GetAllLanguages
from src.language.infrastructure.repositories.sqlmodel_language_repository import SQLLanguageRepository
from src.professional_experience.application.use_cases.get_all_professional_experience import (
    GetAllProfessionalExperience,
)
from src.professional_experience.infrastructure.repositories.sqlmodel_professional_experience_repository import (
    SQLModelProfessionalExperienceRepository,
)
from src.profile.infrastructure.repositories.sqlmodel_profile_repository import (
    SQLModelProfileRepository,
)
from src.resume.application.use_cases.i_resume_generator import IResumeGenerator
from src.resume.infrastructure.pdf_resume_generator import PDFResumeGenarator
from src.resume_focus import ResumeFocus
from src.resume.application.use_cases.get_resume import GetResume, GetResumeParams
from src.profile.application.use_cases.get_profile_by_id import GetProfileById
from src.skills.application.use_cases.find_skills import FindSkillLikeName
from src.skills.infrastructure.repositories.sqlmodel_skill_repository import (
    SkillRepository,
)
from src.tech_profile.application.use_cases.get_tech_profiles import GetTechProfiles
from src.tech_profile.infrastructure.repositories.sqlmodel_profile_repository import (
    SQLModelTechProfileRepository,
)


router = APIRouter()
router.prefix = "/resume"


class Language(Enum):
    EN = "en"
    ES = "es"

def get_get_resume_usecase(session)->GetResume:
    profile_repo = SQLModelProfileRepository(session)
    tech_profile_repo = SQLModelTechProfileRepository(session)
    skill_repo = SkillRepository(session=session)
    professional_experience_repo = SQLModelProfessionalExperienceRepository(
        session=session
    )
    education_repo = SQLModelEducationRepository(session=session)
    language_repo = SQLLanguageRepository(session=session)

    get_profile_by_id = GetProfileById(profile_repo)
    get_tech_profile_by_id = GetTechProfiles(tech_profile_repo)
    find_skill_by_id = FindSkillLikeName(skill_repo)
    get_all_professional_experience = GetAllProfessionalExperience(
        professional_experience_repo
    )
    get_all_education = GetEducationList(education_repo)
    get_all_language = GetAllLanguages(language_repo)
    return GetResume(
        get_profile_by_id,
        get_tech_profile_by_id,
        find_skill_by_id,
        get_all_professional_experience,
        get_all_education,
        get_all_language
    )

@router.get("/")
def get_resume(
    skill_list: list[str] = Query(),
    resume_focus: ResumeFocus = ResumeFocus.JS_FULL_STACK,
    session=Depends(get_session),
):
    get_resume_usecase = get_get_resume_usecase(session)
    resume_data = get_resume_usecase.execute(
        GetResumeParams(
            UUID("9544d18d3a55420bb316b74aab2d0e6f"),
            resume_focus.value,
            skills_list=skill_list,
        )
    )
    resume_genrator: IResumeGenerator = PDFResumeGenarator()
    if resume_data is None:
        raise HTTPException(
            status_code=INTERNAL_SERVER_ERROR,
        )
    pdf_bytes = resume_genrator.generate(resume_data)

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=archivo_{resume_focus}.pdf"
        },
    )
