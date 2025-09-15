from uuid import UUID
from src.ddd_components.use_case import UseCase
from src.professional_experience.domain.entities.company import Company
from src.professional_experience.domain.repositories.base_company_repository import BaseCompanyRepository


class GetCompanyById(UseCase[Company, UUID]):
    def __init__(self, repository: BaseCompanyRepository | None = None):
        super().__init__(repository)

    def execute(self,id: UUID) -> Company|None:
        if not self.repository:
            raise Exception('No repository injected')
        item = self.repository.get_by_id(id)
        return item 
