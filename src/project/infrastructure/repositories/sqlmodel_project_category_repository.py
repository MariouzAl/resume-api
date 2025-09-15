
from typing import Optional
from uuid import UUID
from sqlmodel import Session, select
from src.project.domain.entities import ProjectCategory
from src.project.infrastructure.models import ProjectCategory as ProjectCategoryModel

from src.project.domain.repositories.base_project_category_repository import BaseProjectCategoryRepository

class  SQLModelProjectCategoryRepository(BaseProjectCategoryRepository):
    def __init__(self,session:Session):
        super().__init__()
        self.session=session
    
    def add(self, entity: ProjectCategory) -> ProjectCategory:
        model = ProjectCategoryModel(**entity.dict())
        self.session.add(model)
        self.session.commit()
        entity.id = model.id
        return entity

    def get_by_id(self, entity_id: UUID) -> Optional[ProjectCategory]:
        statement = select(ProjectCategoryModel).where(ProjectCategoryModel.id == entity_id)
        project_cat = self.session.exec(statement).first()
        if not project_cat:
            return None
        return ProjectCategory(**project_cat.model_dump())

    def get_all(self) -> list[ProjectCategory]:
        statement = select(ProjectCategoryModel)
        list_pe=self.session.exec(statement).all()
        return [ProjectCategory(id=pe.id, name=pe.name) for pe in list_pe ]

    def update(self, entity: ProjectCategory) -> ProjectCategory|None:
        pass

    def delete(self, id: UUID) -> None:
        pass

    def filter_by(self, **kwargs) -> list[ProjectCategory]:
        return []
