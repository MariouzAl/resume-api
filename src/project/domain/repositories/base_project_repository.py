from uuid import UUID
from src.ddd_components.base_repository import BaseRepository
from src.project.domain.entities.project import Project


class BaseProjectRepository(BaseRepository[Project, UUID]):
    def __init__(self):
        super().__init__()
