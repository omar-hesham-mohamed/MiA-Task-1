from abc import ABC, abstractmethod

class Racer(ABC):

    @property
    @abstractmethod
    def _fuel(self) -> int:
        pass
    
    @property
    @abstractmethod
    def _tireHealth(self) -> int:
        pass

    @_tireHealth.setter
    @abstractmethod
    def _tireHealth(self, value: int) -> None:
        pass
    
    @property
    @abstractmethod
    def _defCount(self) -> int:
        pass


    @abstractmethod
    def offence(self, id: int) -> int:
        pass
    
    @abstractmethod
    def defence(self, id: int) -> int:
        pass
