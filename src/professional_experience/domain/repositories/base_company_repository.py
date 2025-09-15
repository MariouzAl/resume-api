from uuid import UUID
from src.ddd_components.base_repository import BaseRepository
from src.professional_experience.domain.entities.company import Company


class BaseCompanyRepository(BaseRepository[Company, UUID]):
    def __init__(self):
        super().__init__()
