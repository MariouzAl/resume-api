from src.professional_experience.domain.entities.company_type import CompanyType
from src.professional_experience.infrastructure.models.professional_experience_model import (
    Company as CompanySQLModel,
)
from src.professional_experience.domain.entities import Company


def map_to_company_domain(model: CompanySQLModel) -> Company:
    return Company(
        id=model.id,
        name=model.name,
        company_type=CompanyType(
            id=model.company_type.id, name=model.company_type.name
        ),
    )
