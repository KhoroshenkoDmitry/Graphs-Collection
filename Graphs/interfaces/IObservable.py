from abc import ABC, abstractmethod
from IObserver import IObserver

class IObservable(ABC):
    
    @abstractmethod 
    def notify_observers(self, upd_type: str, upd_values = []) -> None:
         pass

    @abstractmethod 
    def notify_observers(self, commands = []) -> None:
         pass

    @abstractmethod
    def subscribe_observer(self, observer: IObserver) -> None:
         pass




