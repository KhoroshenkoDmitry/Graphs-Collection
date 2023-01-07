from abc import ABC, abstractmethod

class INormalizator(ABC):
    @abstractmethod 
    def normalize(self, input: list) -> list:
        pass


