from uuid import UUID
from src.ddd_components.use_case import UseCase
from src.language.domain.base_language_repository import BaseLanguageRepository
from src.language.domain.entities.language_entity import Language



class AddLanguage(UseCase[Language,UUID]):
    def __init__(self, repository: BaseLanguageRepository):
        super().__init__(repository)

    def execute(self, language: Language)-> Language|None:
        if not self.repository:
            return None
        return self.repository.add(language)
