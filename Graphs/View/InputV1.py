from IInput import IInput

class InputV1(IInput):

    def read(self) -> list:
        string = input().split()
        return self.normalize(string)

    def normalize(self, input: list) -> list:
        input[0] = input[0].casefold()
        return input