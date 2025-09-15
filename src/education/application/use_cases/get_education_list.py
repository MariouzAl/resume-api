from src.ddd_components.use_case import UseCase
from src.education.domain.repositories.base_education_repository import BaseEducationRepository





class GetEducationList(UseCase):
    def __init__(self, repository:BaseEducationRepository|None = None):
        super().__init__(repository)

    def execute(self):
        if(isinstance(self.repository,BaseEducationRepository)):
            education_list=self.repository.get_all()
            return education_list
        
