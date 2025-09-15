from dataclasses import dataclass
from uuid import UUID
from src.ddd_components.use_case import UseCase
from src.profile.domain.entitites import ProfileEntity
from src.profile.domain.repositories.base_profile_repository import (
    BaseProfileRepository,
)


@dataclass
class GetProfileParms:
    id: UUID


class GetProfileById(UseCase):
    def __init__(self, repository: BaseProfileRepository | None = None):
        super().__init__(repository)

    def execute(self, params: GetProfileParms):
        if not isinstance(self.repository, BaseProfileRepository):
            return
        profile: ProfileEntity | None = self.repository.get_by_id(params.id)
        return profile
