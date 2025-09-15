from src.ddd_components.use_case import UseCase
from src.profile.domain.entitites import ProfileEntity
from src.profile.domain.repositories.base_profile_repository import BaseProfileRepository

class GetProfiles(UseCase):
    def __init__(self, repository:BaseProfileRepository|None = None):
        super().__init__(repository)
        
    def execute(self):
        if(not isinstance(self.repository,BaseProfileRepository)):
            return
        profiles:list[ProfileEntity]=self.repository.get_all()
        return profiles