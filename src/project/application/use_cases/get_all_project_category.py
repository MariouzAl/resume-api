from uuid import UUID
from src.ddd_components.base_repository import BaseRepository
from src.ddd_components.use_case import UseCase
from src.project.domain.entities.project_category import (
    ProjectCategory
)

class GetAllProjectCategory(UseCase[ProjectCategory, UUID]):
    def __init__(self, repository: BaseRepository | None = None):
        super().__init__(repository)

    def execute(self) -> list[ProjectCategory] | None:
        if not self.repository:
            return None
        all_items = self.repository.get_all()
        return all_items if all_items is not None else []
