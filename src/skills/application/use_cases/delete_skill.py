from dataclasses import dataclass
from uuid import UUID
from src.ddd_components.use_case import UseCase, UseCaseParams
from src.skills.domain.base_skill_repository import BaseSkillRepository
from src.skills.domain.entities.skill_entity import Skill


@dataclass
class DeleteSkillParams(UseCaseParams):
    id: UUID


class DeleteSkill(UseCase[list[Skill], UUID]):
    def __init__(self, repository: BaseSkillRepository):
        super().__init__(repository)

    def execute(self, param: DeleteSkillParams) -> Skill | None:
        if not self.repository:
            return None
        return self.repository.delete(param.id)
