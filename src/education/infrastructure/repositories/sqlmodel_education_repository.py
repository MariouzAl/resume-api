from datetime import date
from typing import Optional, cast
from uuid import UUID

from sqlalchemy import Column
from sqlmodel import Session, select
from src.education.domain.entities.education_entity import EducationEntity
from src.education.domain.repositories import BaseEducationRepository
from src.education.infrastructure.models.education import Education


class SQLModelEducationRepository(BaseEducationRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def add(self, entity: EducationEntity) -> EducationEntity:
        model = Education(**entity.dict())
        self.session.add(model)
        self.session.commit()
        entity.id = model.id
        return entity

    def get_by_id(self, entity_id: UUID) -> Optional[EducationEntity]:
        statement = select(Education).where(Education.id == entity_id)
        education_item = self.session.exec(statement).first()
        if not education_item:
            return None
        return EducationEntity(**education_item.model_dump())

    def get_all(self) -> list[EducationEntity]:
        ordering_column:Column[date] = cast(Column[date],Education.dateStart)
        statement = select(Education).order_by(ordering_column.desc())
        education_list = self.session.exec(statement).all()
        result_list = [
            EducationEntity(**education_item.model_dump())
            for education_item in education_list
        ]
        return result_list

    def update(self, entity: EducationEntity) -> EducationEntity|None:
        pass

    def delete(self, id: UUID) -> None:
        pass

    def filter_by(self, **kwargs) -> list[EducationEntity]:
        return []
