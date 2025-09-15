from typing import Optional
from uuid import UUID
from sqlmodel import Session, select
from src.professional_experience.domain.entities.company_type import CompanyType
from src.professional_experience.domain.repositories.base_company_type_repository import BaseCompanyTypeRepository
from src.professional_experience.infrastructure.models.professional_experience_model import CompanyType as CompanyTypeModel
from src.professional_experience.infrastructure.mapper import map_to_company_type_domain


class SQLModelCompanyTypeRepository(BaseCompanyTypeRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def add(self, entity: CompanyType) -> CompanyType:
        model = CompanyTypeModel(**entity.dict())
        self.session.add(model)
        self.session.commit()
        entity.id = model.id
        return entity

    def get_by_id(self, entity_id: UUID) -> Optional[CompanyType]:
        statement = select(CompanyTypeModel).where(CompanyTypeModel.id == entity_id)
        company_item = self.session.exec(statement).first()
        if not company_item:
            return None
        return map_to_company_type_domain(company_item)

    def get_all(self) -> list[CompanyType]:
        statement = select(CompanyTypeModel)
        company_list = self.session.exec(statement).all()
        return [map_to_company_type_domain(pe) for pe in company_list]

    def update(self, entity: CompanyType) -> CompanyType | None:
        pass

    def delete(self, id: UUID) -> None:
        statement = select(CompanyTypeModel).where(CompanyTypeModel.id == id)
        company_item = self.session.exec(statement).first()
        if not company_item:
            return None
        self.session.delete(company_item)
        self.session.commit()
        

    def filter_by(self, **kwargs) -> list[CompanyType]:
        return []
