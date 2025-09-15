
from uuid import UUID
from src.ddd_components.use_case import UseCase
from src.project.domain.entities.project_category import ProjectCategory
from src.project.domain.repositories.base_project_category_repository import BaseProjectCategoryRepository


class GetProjectCategoryById(UseCase[ProjectCategory, UUID]):
    def __init__(self, repository: BaseProjectCategoryRepository | None = None):
        super().__init__(repository)

    def execute(self, id: UUID) -> ProjectCategory | None:
        if not self.repository:
            return None
        item = self.repository.get_by_id(entity_id=id)
        return item
