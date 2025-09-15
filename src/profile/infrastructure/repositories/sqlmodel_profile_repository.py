from typing import Optional
from uuid import UUID
from sqlmodel import Session, select
from src.profile.domain.repositories.base_profile_repository import (
    BaseProfileRepository,
)
from src.profile.domain.entitites import ProfileEntity

from ..models import Profile as ProfileSQLModel


class SQLModelProfileRepository(BaseProfileRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def add(self, entity: ProfileEntity) -> ProfileEntity:
        model = ProfileSQLModel(**entity.dict())
        self.session.add(model)
        self.session.commit()
        entity.id=model.id
        return entity

    def get_by_id(self, entity_id: UUID) -> Optional[ProfileEntity]:
        statement = select(ProfileSQLModel).where(ProfileSQLModel.id == entity_id)
        profile = self.session.exec(statement).first()
        print(profile, 'PROFILEEEEEEE')
        if not profile:
            return None
        return ProfileEntity(**profile.model_dump())    

    def get_all(self) -> list[ProfileEntity]:
        statement = select(ProfileSQLModel)
        profile_list = self.session.exec(statement).all()
        entity_list = [ProfileEntity(**profile.model_dump()) for profile in profile_list]
        return entity_list

    def update(self, entity: ProfileEntity) -> Optional[ProfileEntity]:
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

    def filter_by(self, **kwargs) -> list[ProfileEntity]:
        return []
