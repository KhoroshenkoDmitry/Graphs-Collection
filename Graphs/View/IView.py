from abc import abstractmethod
import sys
sys.path.insert(0,'D:/PythonProjects/Graph/interfaces')
sys.path.insert(0,'D:/PythonProjects/Graph/MVC/Model')
sys.path.insert(0,'D:/PythonProjects/Graph/MVC/Controller')
from Interfaces import *
from Model import IModel
from Controller import IController
class IView(IObserver, IObservable):

    __observers: list

    @abstractmethod
    def __init__(self, controller: IController) -> None:
        pass

    @abstractmethod 
    def notify_observers(self, command: list) -> None:
         pass

    @abstractmethod
    def subscribe_observer(self, observer: IObserver) -> None:
         pass

    @abstractmethod
    def update(self, upd_type: str, upd_values: list)-> None:
        pass

    @abstractmethod
    def mainloop(self)->None:
        pass