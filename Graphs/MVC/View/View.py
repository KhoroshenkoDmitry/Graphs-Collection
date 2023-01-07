from IView import *
from OutputV1 import OutputV1
from InputV1 import InputV1
class View(IView):

    def __init__(self, controller: IController) -> None:
        self.__observers = []
        self.subscribe_observer(controller)
        self.output = OutputV1()
        self.input = InputV1()

    def notify_observers(self, command: list) -> None:
        for observer in self.__observers:
            observer.update(command)

    
    def subscribe_observer(self, observer: IObserver) -> None:
         self.__observers.append(observer)

    
    def update(self, upd_type: str, upd_values: list)-> None:
        self.output.update(upd_type, upd_values)

    def mainloop(self) -> None:
        self.output.hello()
        while True:
            command = self.input.read()
            self.notify_observers(command)

            

