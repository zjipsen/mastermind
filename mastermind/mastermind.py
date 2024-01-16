# -*- coding: utf-8 -*-
import sys



class Color:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False


class Feedback(Enum):
    WHITE = 1
    RED = 2


class Code:
    def __init__(self, code: Color[], feedback: Feedback[]=None):
        self.code = code
        self.feedback = feedback

    def generate_feedback(solution: Code):
        sln = solution.deepcopy()

        if len(self.code) != len(solution):
            raise ValueError("Code is a different length than solution.")
        feedback = []
        for color, i in enumerate(self.code):
            if color == solution[i].color:
                sln.remove(color)
                feedback.append(Feedback.RED)
        for color, i in enumerate(self.code):
            if color != solution[i].color and color in sln:  # this is wrong -- should be in solution __ number of times! 
                sln.remove(color) # will this work? they're not the same object
                feedback.append(Feedback.WHITE)





class Mastermind:
    def __init__(self,)



















def play():
    print("Hello World")

def main() -> int:
    """Echo the input arguments to standard output"""
    play()

if __name__ == '__main__':
    sys.exit(main())
