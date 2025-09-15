

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

from src.ddd_components.base_repository import BaseRepository

T = TypeVar("T")
U = TypeVar("U")


class UseCaseParams(ABC):
    pass

class UseCase(ABC, Generic[T,U]):
    def __init__(self, repository: Optional[BaseRepository] = None):
        self.repository:BaseRepository[T,U]|None = repository

    @abstractmethod
    def execute(self,params :Optional[UseCaseParams]) -> Optional[T]:
        pass
    
    