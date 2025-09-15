from dataclasses import dataclass
from uuid import UUID
from src.ddd_components.use_case import UseCase
from src.tech_profile.domain.entitites import TechProfileEntity
from src.tech_profile.domain.repositories.base_profile_repository import BaseTechProfileRepository

@dataclass
class GetProfileParms  :
    id:UUID
    
class GetProfileById(UseCase):
    def __init__(self, repository:BaseTechProfileRepository|None = None):
        super().__init__(repository)
        
    def execute(self,params:GetProfileParms):
        if (not isinstance(self.repository, BaseTechProfileRepository)):
            raise Exception("Not compatible respository")
        profile:TechProfileEntity|None=self.repository.get_by_id(params.id)    
        return profile