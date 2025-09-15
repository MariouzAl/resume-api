from dataclasses import dataclass
from datetime import date
from uuid import UUID, uuid4
from src.ddd_components.use_case import UseCase
from src.skills.domain.base_skill_repository import (
    BaseSkillRepository,
    CreateSkillParams,
)
from src.skills.domain.entities.skill_entity import Skill


class CreateSkill(UseCase[Skill, UUID]):
    def __init__(self, repository: BaseSkillRepository):
        super().__init__(repository)

    def execute(self, skill_param: CreateSkillParams) -> Skill | None:
        if not self.repository:
            return None
        skill = Skill(skill=skill_param.skill, firstUsedDate=skill_param.firstUsedDate,
                      id=uuid4(),level=skill_param.level)
        return self.repository.add(skill)
