from dataclasses import dataclass
from src.ddd_components.use_case import UseCase
from src.tech_profile.domain.entitites import TechProfileEntity
from src.tech_profile.domain.repositories.base_profile_repository import BaseTechProfileRepository

@dataclass
class CreateProfileParams:
    profile:TechProfileEntity
    
    
class CreateProfile(UseCase):
    def __init__(self, repository:BaseTechProfileRepository|None = None):
        super().__init__(repository)
        
    def execute(self,params:CreateProfileParams):
        if (not isinstance(self.repository, BaseTechProfileRepository)):
            raise Exception("Not compatible respository")
        created_profile=self.repository.add(params.profile)
        return created_profile
        