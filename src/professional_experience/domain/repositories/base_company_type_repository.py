from uuid import UUID
from src.ddd_components.base_repository import BaseRepository
from src.professional_experience.domain.entities.company_type import CompanyType


class BaseCompanyTypeRepository(BaseRepository[CompanyType, UUID]):
    def __init__(self):
        super().__init__()
