from datetime import date
from uuid import UUID


class EducationEntity:
    def __init__(
        self,
        title: str,
        dateStart: date,
        dateFinished: date,
        institute: str,
        description: str,
        id: UUID | None=None,
        user_id: UUID | None=None,
    ):
        self.id: UUID | None= id
        self.title: str= title
        self.dateStart: date= dateStart
        self.dateFinished: date= dateFinished
        self.institute: str= institute
        self.description: str= description
        self.user_id: UUID | None= user_id

    def __repr__(self):
        return f"Education Entity (item_id={self.id}, institute={self.institute}, title={self.title},  dateStart={self.dateStart}, dateFinished={self.dateFinished})"
    
        
    def dict(self):
        return self.__dict__