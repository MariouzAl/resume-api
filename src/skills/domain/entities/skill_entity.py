from datetime import date
import uuid


class Skill:
    def __init__(self,  skill: str, level: int, firstUsedDate: date,id: uuid.UUID,):
        self.id: uuid.UUID = id
        self.skill: str = skill
        self.level: int = level
        self.firstUsedDate: date = firstUsedDate

    def __repr__(self):
        return f"Skill Entity (item_id={self.id}, name={self.skill}, price={self.level})"

    def dict(self):
        return self.__dict__
    
    def get_years_of_experience(self):
        today = date.today()
        difference = today-self.firstUsedDate
        years:int = int(difference.days /365)
        difference = difference.days %365
        months = int(difference/30)
        difference = difference %30
        
        return  f"{'+10' if years>10 else years} years" if years >0 else f'{months} months'