from dataclasses import dataclass
from uuid import UUID
from src.ddd_components.use_case import UseCase
from src.education.domain.repositories.base_education_repository import BaseEducationRepository

@dataclass
class GetEducationByIdParams:
    id:UUID



class GetEducationById(UseCase):
    def __init__(self, repository:BaseEducationRepository|None = None):
        super().__init__(repository)

    def execute(self,params:GetEducationByIdParams):
        if(isinstance(self.repository,BaseEducationRepository)):
            education_item=self.repository.get_by_id(params.id)
            return education_item
        
