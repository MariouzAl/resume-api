from dataclasses import dataclass
from uuid import UUID
from src.ddd_components.base_repository import BaseRepository
from src.ddd_components.use_case import UseCase
from src.professional_experience.domain.entities.professional_experience import (
    ProfessionalExperience,
)


@dataclass
class CreateProfessionalExperienceParams:
    item: ProfessionalExperience


class GetAllProfessionalExperience(UseCase[ProfessionalExperience, UUID]):
    def __init__(self, repository: BaseRepository | None = None):
        super().__init__(repository)

    def execute(self) -> list[ProfessionalExperience] | None:
        if not self.repository:
            return None
        all_items = self.repository.get_all()
        return all_items if all_items else []
