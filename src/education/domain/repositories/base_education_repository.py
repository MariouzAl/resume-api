from abc import ABC
import uuid
from src.ddd_components.base_repository import BaseRepository
from src.education.domain.entities.education_entity import EducationEntity


class BaseEducationRepository(BaseRepository[EducationEntity, uuid.UUID],ABC):
    def __init__(self):
        super().__init__()
