import uuid


class TechProfileEntity:
    def __init__(
        self,
        focus: str,
        description: str,
        id: uuid.UUID|None=None,
    ):
        self.id: uuid.UUID|None = id
        self.focus: str = focus
        self.description: str = description


    def __repr__(self):
        return f'Profile entity (id={self.id}, name={self.focus})'
    
    def dict(self):
        return self.__dict__