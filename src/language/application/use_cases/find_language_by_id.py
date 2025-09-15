from dataclasses import dataclass
from uuid import UUID
from src.ddd_components.use_case import UseCase, UseCaseParams
from src.skills.domain.base_skill_repository import BaseSkillRepository
from src.skills.domain.entities import Skill


@dataclass
class FindLanguageByIdParams(UseCaseParams):
    id: UUID


class FindLanguageById(UseCase[Skill,UUID]):
    def __init__(self, repository: BaseSkillRepository):
        super().__init__(repository)

    def execute(self, params: FindLanguageByIdParams)-> Skill|None:
        if(not self.repository):
            return None
        return self.repository.get_by_id(params.id)
