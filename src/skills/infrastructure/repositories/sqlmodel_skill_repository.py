

from sqlmodel import or_
from typing import Optional, cast
from uuid import UUID

from sqlmodel import Session, select, Column
from src.skills.domain.base_skill_repository import BaseSkillRepository
from src.skills.infrastructure.models import Skill as SkillSQLModel
from src.skills.domain.entities import Skill


class SkillRepository (BaseSkillRepository):
    def __init__(self,session:Session):
        super().__init__()
        self.session = session
    
     
    def add(self, entity: Skill) -> Skill:
        model = SkillSQLModel(**entity.dict())
        self.session.add(model)
        self.session.commit()
        return Skill(**model.model_dump())

    
    def get_by_id(self, entity_id: UUID) -> Optional[Skill]:
        statement = select(SkillSQLModel).where(SkillSQLModel.id == entity_id)
        skill=self.session.exec(statement).first()
        if not skill:
            return None
        return Skill(**skill.model_dump())

    
    def get_all(self) -> list[Skill]:
        statement = select(SkillSQLModel)
        skill_list=self.session.exec(statement).all()
        return [Skill(**skill.model_dump()) for skill in skill_list]
    
    def update(self, entity: Skill) -> Skill|None:
        pass

    
    def delete(self, id: UUID) -> None:
        item=self.get_by_id(id)
        self.session.delete(item)
        self.session.commit()

    
    def filter_by(self, **kwargs) -> list[Skill]:
        skill_names:list[str]=kwargs['skill_names']
        skill_column=cast(Column,SkillSQLModel.skill)
        conditions = [skill_column.like(f"%{name}%") for name in skill_names]
        statement = select(SkillSQLModel).where(or_(*conditions))
        skill_list = self.session.exec(statement).all()
        return [Skill(**skill.model_dump()) for skill in skill_list]