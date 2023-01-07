from IValidator import IValidator
from RulesV1 import RulesV1

class ValidatorV1(IValidator):

    def __init__(self) -> None:
        self.__rules = RulesV1()

    def validate(self, input: str) -> bool:
        if input in self.__rules.get_rules():
            return True
        else:
            return False