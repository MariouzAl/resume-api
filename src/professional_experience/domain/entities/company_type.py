from uuid import UUID


class CompanyType:
    def __init__(self, name:str ,id:UUID|None=None) -> None:
        self.id:UUID|None = id
        self.name: str=name
        
    def dict(self):
        return self.__dict__