from abc import ABC, abstractmethod

class IInput(ABC):

    @abstractmethod
    def read(self) -> list:
        pass






