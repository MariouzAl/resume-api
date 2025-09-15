from uuid import UUID
from src.ddd_components.base_repository import BaseRepository
from src.profile.domain.entitites import ProfileEntity


class BaseProfileRepository (BaseRepository[ProfileEntity,UUID]):
    def __init__(self):
        super().__init__()