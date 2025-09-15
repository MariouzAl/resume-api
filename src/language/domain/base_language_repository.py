import uuid
from src.ddd_components.base_repository import BaseRepository
from abc import ABC

from src.language.domain.entities.language_entity import Language



class BaseLanguageRepository(BaseRepository[Language, uuid.UUID], ABC):
    def __init__(self):
        super().__init__()
