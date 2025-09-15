from src.ddd_components.use_case import UseCase
from src.tech_profile.domain.entitites import TechProfileEntity
from src.tech_profile.domain.repositories.base_profile_repository import BaseTechProfileRepository

class GetTechProfiles(UseCase):
    def __init__(self, repository:BaseTechProfileRepository):
        super().__init__(repository)
        
    def execute(self):
        if (not isinstance(self.repository, BaseTechProfileRepository)):
            raise Exception("Not compatible respository")
        profiles:list[TechProfileEntity]=self.repository.get_all()
        return profiles