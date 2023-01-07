from IModel import *
class Model(IModel):

    def __init__(self):
        self.__observers = []
        self.__graphs = GraphCollection()
        self.__commands_for_return = ['get_names','graph_update_is_in_graph','show_graph']
    def notify_observers(self, upd_type: str, upd_values = []) -> None:
        for observer in self.__observers:
                observer.update(upd_type, upd_values)

    def subscribe_observer(self, observer: IObserver) -> None:
        self.__observers.append(observer)

    def update(self, upd_type: str, upd_values = []) -> None:
        value = self.__graphs.update(upd_type, upd_values)
        if upd_type in self.__commands_for_return:
            upd_values.append(value)
        self.notify_observers(upd_type, upd_values)


