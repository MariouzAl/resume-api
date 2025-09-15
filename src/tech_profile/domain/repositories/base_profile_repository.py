from uuid import UUID
from src.ddd_components.base_repository import BaseRepository
from src.tech_profile.domain.entitites import TechProfileEntity


class BaseTechProfileRepository (BaseRepository[TechProfileEntity,UUID]):
    def __init__(self):
        super().__init__()