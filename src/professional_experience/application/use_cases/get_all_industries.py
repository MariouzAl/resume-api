from uuid import UUID
from src.ddd_components.use_case import UseCase
from src.professional_experience.domain.entities.company_type import CompanyType
from src.professional_experience.domain.repositories.base_company_type_repository import BaseCompanyTypeRepository


class GetAllIndustries(UseCase[CompanyType, UUID]):
    
    def __init__(self, repository: BaseCompanyTypeRepository | None = None):
        super().__init__(repository)

    def execute(self) -> list[CompanyType]:
        if not self.repository:
            raise Exception('No repository injected')
        all_items = self.repository.get_all()
        return all_items if all_items else []
