from src.ddd_components.use_case import UseCase
from src.skills.domain.base_skill_repository import BaseSkillRepository
from src.skills.domain.entities import Skill


class GetAllSkills(UseCase):
    def __init__(self, repository: BaseSkillRepository):
        super().__init__(repository)

    def execute(self) -> list[Skill]:
        if not self.repository:
            return []
        skills = self.repository.get_all()
        return skills
