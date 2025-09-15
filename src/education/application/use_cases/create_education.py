from dataclasses import dataclass
from src.ddd_components.use_case import UseCase
from src.education.domain.entities import EducationEntity
from src.education.domain.repositories.base_education_repository import BaseEducationRepository


@dataclass
class CreateEducationParams:
    education_item: EducationEntity


class CreateEducation(UseCase):
    def __init__(self, repository:BaseEducationRepository|None = None):
        super().__init__(repository)

    def execute(self, params: CreateEducationParams):
        if (not isinstance(self.repository, BaseEducationRepository)):
            raise Exception("Not compatible respository")
        created_education_item=self.repository.add(params.education_item)
        return created_education_item
        
