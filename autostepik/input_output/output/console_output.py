from .output import Output

class ConsoleOutput(Output):
    @staticmethod
    def print(string):
        print(string, end="")