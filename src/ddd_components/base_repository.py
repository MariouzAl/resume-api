from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional

# Definimos TypeVars genéricos para la entidad y su ID
T = TypeVar('T')
U = TypeVar('U')

class BaseRepository(ABC, Generic[T, U]):
    """
    Clase abstracta para un repositorio genérico.
    Define una interfaz para las operaciones de persistencia.
    """

    @abstractmethod
    def add(self, entity: T) -> T:
        pass

    @abstractmethod
    def get_by_id(self, entity_id: U) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, id: U) -> None:
        pass

    @abstractmethod
    def filter_by(self, **kwargs) -> List[T]:
        pass