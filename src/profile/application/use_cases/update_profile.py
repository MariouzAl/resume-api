from dataclasses import dataclass
from src.ddd_components.use_case import UseCase
from src.profile.domain.entitites import ProfileEntity
from src.profile.domain.repositories.base_profile_repository import BaseProfileRepository

@dataclass
class UpdateProfileParams:
    profile:ProfileEntity
    
    
class UpdateProfile(UseCase):
    def __init__(self, repository:BaseProfileRepository = None):
        super().__init__(repository)
        
    def execute(self,params:UpdateProfileParams):
        if (not isinstance(self.repository, BaseProfileRepository)):
            raise Exception("Not compatible respository")
        updated_profile=self.repository.update(params.profile)
        return updated_profile
        