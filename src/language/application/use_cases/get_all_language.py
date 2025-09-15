from src.ddd_components.use_case import UseCase
from src.language.domain.base_language_repository import BaseLanguageRepository
from src.language.domain.entities.language_entity import Language


class GetAllLanguages(UseCase):
    def __init__(self, repository: BaseLanguageRepository):
        super().__init__(repository)

    def execute(self) -> list[Language]:
        if not self.repository:
            return []
        skills = self.repository.get_all()
        return skills
