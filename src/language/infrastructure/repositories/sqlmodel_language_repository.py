

from sqlmodel import or_
from typing import Optional, cast
from uuid import UUID

from sqlmodel import Session, select, Column

from src.language.domain.base_language_repository import BaseLanguageRepository
from src.language.domain.entities.language_entity import Language
from src.language.infrastructure.models.language import Language as LanguageSQLModel

class SQLLanguageRepository (BaseLanguageRepository):
    def __init__(self,session:Session):
        super().__init__()
        self.session = session
    
     
    def add(self, entity: Language) -> Language:
        model = LanguageSQLModel(**entity.dict())
        self.session.add(model)
        self.session.commit()
        return Language(**model.model_dump())

    
    def get_by_id(self, entity_id: UUID) -> Optional[Language]:
        statement = select(LanguageSQLModel).where(LanguageSQLModel.id == entity_id)
        language=self.session.exec(statement).first()
        if not language:
            return None
        return Language(**language.model_dump())

    
    def get_all(self) -> list[Language]:
        statement = select(LanguageSQLModel)
        language_list=self.session.exec(statement).all()
        return [Language(**language.model_dump()) for language in language_list]
    
    def update(self, entity: Language) -> Language|None:
        pass

    
    def delete(self, id: UUID) -> None:
        item=self.get_by_id(id)
        self.session.delete(item)
        self.session.commit()

    
    def filter_by(self, **kwargs) -> list[Language]:
        language_names:list[str]=kwargs['language_names']
        language_column=cast(Column,LanguageSQLModel.language)
        conditions = [language_column.like(f"%{name}%") for name in language_names]
        statement = select(LanguageSQLModel).where(or_(*conditions))
        language_list = self.session.exec(statement).all()
        return [Language(**language.model_dump()) for language in language_list]