
from src.education.domain.entities.education_entity import EducationEntity
from src.language.domain.entities.language_entity import Language
from src.professional_experience.domain.entities.company_type import CompanyType
from src.professional_experience.domain.entities.professional_experience import ProfessionalExperience
from src.profile.domain.entitites.profile_entity import ProfileEntity
from src.resume_focus import ResumeFocus
from src.skills.domain.entities.skill_entity import Skill
from src.tech_profile.domain.entitites.tech_profile_entity import TechProfileEntity


def get_focus(focus : str)->str:
    if focus ==ResumeFocus.JS_FULL_STACK.value:
        return "Nodejs Fullstack Developer"
    if focus ==ResumeFocus.JS_FRONTEND:
        return "Frontend Developer"
    if focus ==ResumeFocus.PYTHON.value:
        return "Python Developer"
    return "Software Engineer"
    


class ResumeEntity:
    def __init__(self,
        focus:str,
        profile :ProfileEntity,
        tech_profile :TechProfileEntity,
        skills : list[Skill],
        professional_experiences:list[ProfessionalExperience],
        education:list[EducationEntity],
        languages :list[Language],
        industries:list[CompanyType]
                 ) -> None:
            self.focus=get_focus(focus)
            self.profile=profile
            self.tech_profile=tech_profile
            self.skills=skills
            self.professional_experiences=professional_experiences
            self.education=education
            self.languages=languages
            self.industries=industries