from .input import Input

class ConsoleInput(Input):
    @staticmethod
    def read_line():
        return input()