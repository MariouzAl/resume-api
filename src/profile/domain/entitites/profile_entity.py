from datetime import date
import uuid


class ProfileEntity:
    def __init__(
        self,
        name: str,
        birthday: date,
        phone: str,
        city: str,
        email: str,
        freelance: str,
        degree: str,
        description: str,
        id: uuid.UUID|None=None,
    ):
        self.id: uuid.UUID|None = id
        self.name: str = name
        self.birthday: date = birthday
        self.phone: str = phone
        self.city: str = city
        self.email: str = email
        self.freelance: str = freelance
        self.degree: str = degree
        self.description: str = description


    def __repr__(self):
        return f'Profile entity (id={self.id}, name={self.name}, email={self.email})'
    
    def dict(self):
        return self.__dict__