
from typing import Optional, cast
from uuid import UUID
from sqlmodel import  Session, select, Column
from src.professional_experience.domain.repositories.base_professional_experience_repository import BaseProfessionalExperienceRepository
from src.professional_experience.domain.entities import ProfessionalExperience
from src.professional_experience.infrastructure.models import ProfessionalExperience as ProfessionalExperienceModel
from src.professional_experience.infrastructure.mapper import map_to_professional_experience_domain

class  SQLModelProfessionalExperienceRepository(BaseProfessionalExperienceRepository):
    def __init__(self,session:Session):
        super().__init__()
        self.session=session
    
    def add(self, entity: ProfessionalExperience) -> ProfessionalExperience:
        model = ProfessionalExperience(**entity.dict())
        self.session.add(model)
        self.session.commit()
        entity.id = model.id
        return entity

    def get_by_id(self, entity_id: UUID) -> Optional[ProfessionalExperience]:
        """ statement = select(Education).where(Education.id == entity_id)
        education_item = self.session.exec(statement).first()
        if not education_item:
            return None
        return ProfessionalExperience(**education_item.model_dump()) """
        pass

    def get_all(self) -> list[ProfessionalExperience]:
        start_date_col =cast(Column,ProfessionalExperienceModel.startDate)
        end_date_col =cast(Column,ProfessionalExperienceModel.endDate)
        statement = select(ProfessionalExperienceModel).order_by(start_date_col.desc(),end_date_col.desc())
        list_pe=self.session.exec(statement).all()
        return [map_to_professional_experience_domain(pe) for pe in list_pe ]

    def update(self, entity: ProfessionalExperience) -> ProfessionalExperience|None:
        pass

    def delete(self, id: UUID) -> None:
        pass

    def filter_by(self, **kwargs) -> list[ProfessionalExperience]:
        return []
