from abc import ABC, abstractmethod
class IObserver(ABC):
    
    @abstractmethod
    def update(self, upd_type: str, upd_values: list)-> None:
        pass

    @abstractmethod
    def update(self,command = [])->None:
        pass





