from IController import *
from NormalizatorV1 import NormalizatorV1
from ValidatorV1 import ValidatorV1

class Controller(IController):

    def __init__(self, model: IModel) -> None:
        self.__observers = []
        self.subscribe_observer(model)
        self.validator = ValidatorV1()
        self.normalizator = NormalizatorV1()

    def separate_dimensions(self, upd_type: str, upd_values: list) -> None:
        if upd_type != 'exit':
            self.notify_observers(upd_type, upd_values)
        else:
            exit()

    def notify_observers(self, upd_type: str, upd_values = []) -> None:
        for observer in self.__observers:
            observer.update(upd_type, upd_values)


    def subscribe_observer(self, observer: IObserver) -> None:
         self.__observers.append(observer)


    def update(self, command: list)-> None:
        normalized_command = self.normalizator.normalize(command)
        is_valid = self.validator.validate( normalized_command[0])
        if is_valid:
            self.separate_dimensions(normalized_command[0],normalized_command[1:])
        else:
            raise NotImplementedError(f'{normalized_command[0]} does not exist! Please, type "help" to get more info.')





