from abc import ABC, abstractmethod

class IOutput(ABC):

    @abstractmethod
    def output(string: str) -> None:
        pass


