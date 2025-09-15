from uuid import UUID
from src.ddd_components.use_case import UseCase
from src.project.domain.entities import Project
from src.project.domain.repositories import BaseProjectRepository


class GetAllProjects(UseCase[Project, UUID]):
    def __init__(self, repository: BaseProjectRepository | None = None):
        super().__init__(repository)

    def execute(self) -> list[Project]:
        if not self.repository:
            raise Exception('No repository injected')
        all_items = self.repository.get_all()
        return all_items if all_items else []
