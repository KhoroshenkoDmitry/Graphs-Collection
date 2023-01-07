from GraphCollection import GraphCollection
from abc import ABC, abstractmethod
import sys
sys.path.insert(0,'D:/PythonProjects/Graph/interfaces')
from Interfaces import *

class IModel(IObserver, IObservable):
    __graphs: GraphCollection
    __observers: list

    @abstractmethod 
    def notify_observers(self, upd_type: str, upd_values = []) -> None:
         pass

    @abstractmethod
    def subscribe_observer(self, observer: IObserver) -> None:
         pass

    @abstractmethod
    def update(self, upd_type: str, upd_values: list)-> None:
        pass





