from uuid import UUID
from src.ddd_components.base_repository import BaseRepository
from src.project.domain.entities.project_category import ProjectCategory



class BaseProjectCategoryRepository (BaseRepository[ProjectCategory,UUID]):
    def __init__(self):
        super().__init__()