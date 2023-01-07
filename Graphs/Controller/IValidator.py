from abc import ABC, abstractmethod
from IRules import IRules

class IValidator(ABC):

    __rules: IRules

    @abstractmethod 
    def validate(self, input: str) -> bool:
        pass



