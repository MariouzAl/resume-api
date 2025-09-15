from typing import Optional
from uuid import UUID
from sqlmodel import Session, select
from src.professional_experience.domain.repositories.base_company_repository import (
    BaseCompanyRepository,
)
from src.professional_experience.domain.entities import Company
from src.professional_experience.infrastructure.models.professional_experience_model import Company as CompanyModel
from src.professional_experience.infrastructure.mapper import map_to_company_domain


class SQLModelCompanyRepository(BaseCompanyRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def add(self, entity: Company) -> Company:
        model = CompanyModel(**entity.dict())
        self.session.add(model)
        self.session.commit()
        entity.id = model.id
        return entity

    def get_by_id(self, entity_id: UUID) -> Optional[Company]:
        statement = select(CompanyModel).where(CompanyModel.id == entity_id)
        company_item = self.session.exec(statement).first()
        if not company_item:
            return None
        return map_to_company_domain(company_item)

    def get_all(self) -> list[Company]:
        statement = select(CompanyModel)
        company_list = self.session.exec(statement).all()
        return [map_to_company_domain(pe) for pe in company_list]

    def update(self, entity: Company) -> Company | None:
        pass

    def delete(self, id: UUID) -> None:
        statement = select(CompanyModel).where(CompanyModel.id == id)
        company_item = self.session.exec(statement).first()
        if not company_item:
            return None
        self.session.delete(company_item)
        self.session.commit()
        

    def filter_by(self, **kwargs) -> list[Company]:
        return []
