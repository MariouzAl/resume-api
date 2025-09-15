from dataclasses import dataclass
from uuid import UUID
from src.ddd_components.base_repository import BaseRepository
from src.ddd_components.use_case import UseCase
from src.project.domain.entities.project import (
    Project
)


@dataclass
class CreateProjectParams:
    item: Project


class CreateProject(UseCase[Project, UUID]):
    def __init__(self, repository: BaseRepository | None = None):
        super().__init__(repository)

    def execute(self, params: CreateProjectParams) -> Project | None:
        if not self.repository:
            return None
        created_item = self.repository.add(params.item)
        return created_item