from uuid import UUID
from src.ddd_components.base_repository import BaseRepository
from src.professional_experience.domain.entities.professional_experience import ProfessionalExperience



class BaseProfessionalExperienceRepository (BaseRepository[ProfessionalExperience,UUID]):
    def __init__(self):
        super().__init__()