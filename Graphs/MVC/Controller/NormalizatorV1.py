from INormalizator import INormalizator

class NormalizatorV1(INormalizator):
    def normalize(self, input: list) -> list:
        input[0] = input[0].casefold()
        return input