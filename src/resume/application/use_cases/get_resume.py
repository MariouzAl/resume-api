from dataclasses import dataclass
from uuid import UUID
from src.ddd_components.use_case import UseCase
from src.education.application.use_cases.get_education_list import GetEducationList
from src.language.application.use_cases.get_all_language import GetAllLanguages
from src.professional_experience.application.use_cases.get_all_professional_experience import (
    GetAllProfessionalExperience,
)
from src.professional_experience.domain.entities.professional_experience import ProfessionalExperience
from src.resume.domain.entities.resume import ResumeEntity
from src.skills.application.use_cases.find_skills import (
    FindSkillLikeName,
    FindSkillParams,
)
from src.tech_profile.application.use_cases.get_tech_profiles import GetTechProfiles
from src.profile.application.use_cases.get_profile_by_id import (
    GetProfileById,
    GetProfileParms,
)


@dataclass
class GetResumeParams:
    id: UUID
    focus: str
    skills_list: list[str]


class GetResume(UseCase):
    def __init__(
        self,
        get_profile_use_case: GetProfileById,
        get_tech_profile_use_case: GetTechProfiles,
        find_skills_use_case: FindSkillLikeName,
        get_professional_experiences_use_case: GetAllProfessionalExperience,
        get_all_education : GetEducationList,
        get_all_language : GetAllLanguages
    ):
        self.get_profile_use_case = get_profile_use_case
        self.get_tech_profile_use_case = get_tech_profile_use_case
        self.find_skills_use_case = find_skills_use_case
        self.get_professional_experiences_use_case = (
            get_professional_experiences_use_case
        )
        self.get_all_education=get_all_education
        self.get_all_language_use_case=get_all_language

    def execute(self, params: GetResumeParams) -> ResumeEntity | None:
        profile = self.get_profile_use_case.execute(params=GetProfileParms(params.id))
        if profile is None:
            return None
        tech_profile = self.get_tech_profile_use_case.execute()
        skills = self.find_skills_use_case.execute(
            FindSkillParams(skill_names=params.skills_list)
        )
        skills = skills if skills is not None else []
        professional_experiences_result = self.get_professional_experiences_use_case.execute()
        professional_experiences: list[ProfessionalExperience] = professional_experiences_result if professional_experiences_result is not None else []
        education_response = self.get_all_education.execute() 
        education=education_response if education_response is not None else []
        languages = self.get_all_language_use_case.execute()
        resume: ResumeEntity = ResumeEntity(
            focus=params.focus,
            profile=profile,
            tech_profile=tech_profile[0],
            skills=skills,
            professional_experiences=professional_experiences,
            education=education,
            languages=languages
        )
        return resume
