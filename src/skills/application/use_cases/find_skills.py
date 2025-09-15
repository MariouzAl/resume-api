from dataclasses import dataclass
from uuid import UUID
from src.ddd_components.use_case import UseCase, UseCaseParams
from src.skills.domain.base_skill_repository import BaseSkillRepository
from src.skills.domain.entities import Skill


@dataclass
class FindSkillParams(UseCaseParams):
    skill_names:list[str]


class FindSkillLikeName(UseCase[Skill,UUID]):
    def __init__(self, repository: BaseSkillRepository):
        super().__init__(repository)

    def execute(self, params: FindSkillParams)-> list[Skill]|None:
        if(not self.repository):
            return
        return self.repository.filter_by(skill_names=params.skill_names)
