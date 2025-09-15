from datetime import date
from uuid import UUID


from .project_category import  ProjectCategory



class Project:
    def __init__(
        self,
        id: UUID|None,
        project: str,
        shortDescription: str,
        fullDescription: str,
        link: str,
        projectLink: str, 
        categories: list[ProjectCategory],
        cover: str, 
        builtWith: list[str], 
        images: list[str],
        key: str,
        start_date:date,
        end_date:date,
        professional_experience_id: UUID|None,
        responsibilities:list[str] =[]
    ) -> None:
        self.id: UUID|None=id
        self.project: str=project
        self.shortDescription: str=shortDescription
        self.fullDescription: str=fullDescription
        self.link: str=link
        self.projectLink: str=projectLink
        self.categories: list[ProjectCategory]=categories
        self.cover: str=cover
        self.builtWith: list[str]=builtWith
        self.images: list[str]=images
        self.key: str=key
        self.start_date :date =start_date 
        self.end_date :date =end_date
        self.professional_experience_id: UUID|None=professional_experience_id
        self.responsibilities =responsibilities
          
    
    def dict (self):
        return self.__dict__