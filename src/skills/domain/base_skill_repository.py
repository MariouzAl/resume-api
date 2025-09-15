from dataclasses import dataclass
from datetime import date
import uuid
from src.ddd_components.base_repository import BaseRepository
from abc import ABC

from src.ddd_components.use_case import UseCaseParams
from src.skills.domain.entities import Skill

@dataclass
class CreateSkillParams(UseCaseParams):
    skill: str
    level: int
    firstUsedDate: date
    


class BaseSkillRepository(BaseRepository[Skill, uuid.UUID], ABC):
    def __init__(self):
        super().__init__()
