from dataclasses import dataclass
from src.ddd_components.use_case import UseCase
from src.tech_profile.domain.entitites import TechProfileEntity
from src.tech_profile.domain.repositories.base_profile_repository import BaseTechProfileRepository

@dataclass
class UpdateProfileParams:
    profile:TechProfileEntity
    
    
class UpdateProfile(UseCase):
    def __init__(self, repository:BaseTechProfileRepository|None = None):
        super().__init__(repository)
        
    def execute(self,params:UpdateProfileParams):
        if (not isinstance(self.repository, BaseTechProfileRepository)):
            raise Exception("Not compatible respository")
        updated_profile=self.repository.update(params.profile)
        return updated_profile
        