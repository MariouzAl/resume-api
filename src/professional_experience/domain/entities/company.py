from uuid import UUID

from src.professional_experience.domain.entities.company_type import CompanyType


class Company:
    def __init__(self, name:str ,company_type:CompanyType|None = None,id:UUID|None=None) -> None:
        self.id:UUID|None = id
        self.name: str=name
        self.company_type: CompanyType|None= company_type
        
    def dict(self):
        return self.__dict__