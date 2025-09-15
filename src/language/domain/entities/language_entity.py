import uuid


class Language:
    def __init__(self,  language: str, level: str,id: uuid.UUID|None=None,):
        self.id: uuid.UUID|None = id
        self.language: str = language
        self.level: str = level

    def __repr__(self):
        return f"Skill Entity (item_id={self.id}, name={self.language}, price={self.level})"

    def dict(self):
        return self.__dict__
