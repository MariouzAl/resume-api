from typing import Optional
from uuid import UUID
from sqlmodel import Session, select
from src.tech_profile.domain.repositories.base_profile_repository import ( BaseTechProfileRepository
)
from src.tech_profile.domain.entitites import TechProfileEntity

from ..models import TechProfile as TechProfileSQL


class SQLModelTechProfileRepository(BaseTechProfileRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def add(self, entity: TechProfileEntity) -> TechProfileEntity:
        model = TechProfileSQL(**entity.dict())
        self.session.add(model)
        self.session.commit()
        entity.id=model.id
        return entity

    def get_by_id(self, entity_id: UUID) -> Optional[TechProfileEntity]:
        statement = select(TechProfileSQL).where(TechProfileSQL.id == entity_id)
        profile = self.session.exec(statement).first()
        if not profile:
            return None
        return TechProfileEntity(**profile.model_dump())    

    def get_all(self) -> list[TechProfileEntity]:
        statement = select(TechProfileSQL)
        profile_list = self.session.exec(statement).all()
        entity_list = [TechProfileEntity(**profile.model_dump()) for profile in profile_list]
        return entity_list

    def update(self, entity: TechProfileEntity) -> Optional[TechProfileEntity]:
        if entity.id:
            model = self.get_by_id(entity.id)
            if model is None:
                return None
            # Define the attributes you want to update
            fields_to_update = [
                "birthday",
                "city",
                "degree",
                "description",
                "email",
                "freelance",
                "name",
                "phone",
            ]
            # Iterate and update the model's attributes
            for field in fields_to_update:
                new_value = getattr(entity, field)
                setattr(model, field, new_value)
            self.session.add(model)
            self.session.commit()
            return entity

    def delete(self, id: UUID) -> None:
        item = self.get_by_id(id)
        self.session.delete(item)
        self.session.commit()

    def filter_by(self, **kwargs) -> list[TechProfileEntity]:
        return []
