from src.professional_experience.domain.entities.company_type import CompanyType
from src.professional_experience.infrastructure.models.professional_experience_model import CompanyType as CompanyTypeSQLModel



def map_to_company_type_domain(
    model: CompanyTypeSQLModel
) -> CompanyType:
    return CompanyType(id=model.id, name=model.name)
    