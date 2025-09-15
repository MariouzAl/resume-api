from typing import Optional, cast
from uuid import UUID
from sqlmodel import Session, select,Column
from src.project.domain.repositories.base_project_repository import (
    BaseProjectRepository,
)
from src.project.infrastructure.models.project import Project as ProjectModel
from src.project.infrastructure.mapper import map_to_project_domain
from src.project.domain.entities.project import Project


class SQLModelProjectRepository(BaseProjectRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def add(self, entity: Project) -> Project:
        model = ProjectModel(**entity.dict())
        self.session.add(model)
        self.session.commit()
        entity.id = model.id
        return entity

    def get_by_id(self, entity_id: UUID) -> Optional[Project]:
        statement = select(ProjectModel).where(ProjectModel.id == entity_id)
        company_item = self.session.exec(statement).first()
        if not company_item:
            return None
        return map_to_project_domain(company_item)

    def get_all(self) -> list[Project]:
        start_date_col:Column =cast(Column,ProjectModel.start_date)
        end_date_col:Column =cast(Column,ProjectModel.end_date)
        statement = select(ProjectModel).order_by(start_date_col.desc(),end_date_col.desc())
        company_list = self.session.exec(statement).all()
        return [map_to_project_domain(pe) for pe in company_list]

    def update(self, entity: Project) -> Project | None:
        pass

    def delete(self, id: UUID) -> None:
        statement = select(ProjectModel).where(ProjectModel.id == id)
        company_item = self.session.exec(statement).first()
        if not company_item:
            return None
        self.session.delete(company_item)
        self.session.commit()
        

    def filter_by(self, **kwargs) -> list[Project]:
        return []
