from dataclasses import dataclass
from src.ddd_components.use_case import UseCase
from src.profile.domain.entitites import ProfileEntity
from src.profile.domain.repositories.base_profile_repository import BaseProfileRepository

@dataclass
class CreateProfileParams:
    profile:ProfileEntity
    
    
class CreateProfile(UseCase):
    def __init__(self, repository:BaseProfileRepository|None = None):
        super().__init__(repository)
        
    def execute(self,params:CreateProfileParams):
        if (not isinstance(self.repository, BaseProfileRepository)):
            raise Exception("Not compatible respository")
        created_profile=self.repository.add(params.profile)
        return created_profile
        