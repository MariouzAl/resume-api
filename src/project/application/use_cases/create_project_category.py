from dataclasses import dataclass
from uuid import UUID
from src.ddd_components.use_case import UseCase
from src.project.domain.entities.project_category import ProjectCategory
from src.project.domain.repositories.base_project_category_repository import BaseProjectCategoryRepository


@dataclass
class CreateProjectCategoryParams:
    name: str


class CreateProjectCategory(UseCase[ProjectCategory, UUID]):
    def __init__(self, repository: BaseProjectCategoryRepository | None = None):
        super().__init__(repository)

    def execute(self, params: CreateProjectCategoryParams) -> ProjectCategory | None:
        if not self.repository:
            return None
        created_item = self.repository.add(ProjectCategory(name=params.name))
        return created_item