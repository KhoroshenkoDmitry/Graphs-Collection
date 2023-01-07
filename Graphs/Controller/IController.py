from abc import abstractmethod
import sys
sys.path.insert(0,'D:/PythonProjects/Graph/interfaces')
sys.path.insert(0,'D:/PythonProjects/Graph/MVC/Model')
from Interfaces import *
from Model import IModel

class IController(IObserver, IObservable):

    __observers: list

    @abstractmethod
    def __init__(self, model: IModel) -> None:
        pass

    @abstractmethod 
    def notify_observers(self, upd_type: str, upd_values = []) -> None:
         pass

    @abstractmethod
    def subscribe_observer(self, observer: IObserver) -> None:
         pass

    @abstractmethod
    def update(self, command: list)-> None:
        pass



