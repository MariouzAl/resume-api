from dataclasses import dataclass
from uuid import UUID
from src.ddd_components.use_case import UseCase
from src.professional_experience.domain.entities.company import Company
from src.professional_experience.domain.repositories.base_company_repository import BaseCompanyRepository


@dataclass
class RegisterCompanyParams:
    name: str
    company_type_id : UUID


class RegisterCompany(UseCase[Company, UUID]):
    def __init__(self, repository: BaseCompanyRepository | None = None):
        super().__init__(repository)

    def execute(self, params: RegisterCompanyParams) -> Company | None:
        if not self.repository:
            return None
        created_item = self.repository.add(Company(name=params.name))
        return created_item