from datetime import date
from uuid import UUID

from src.project.domain.entities.project import Project

from .company import Company


class ProfessionalExperience:
    def __init__(
        self,
        id: UUID | None,
        key: str,
        company_id: UUID,
        company: Company,
        startDate: date,
        endDate: date,
        position: str,
        projects: list[Project]|None,
    ) -> None:
        self.id: UUID | None = id
        self.key: str = key
        self.company_id: UUID = company_id
        self.company: Company = company
        self.startDate: date = startDate
        self.endDate: date = endDate
        self.position: str = position
        self.projects: list[Project]|None = projects

    def dict(self):
        return self.__dict__
