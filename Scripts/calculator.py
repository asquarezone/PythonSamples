class Calculator:

    def __init__(self, numbers):
        """
        initialization of Calculator
        :param numbers: list of numbers
        """
        self.numbers = numbers

    def add(self):
        result = 0
        for number in self.numbers:
            result = result + number
        return result

    def mul(self):
        result = 1
        for number in self.numbers:
            result = result * number
        return result
