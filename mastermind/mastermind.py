# -*- coding: utf-8 -*-
from enum import Enum
from typing import List

import click
import copy
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
    def __init__(self, code: List[Color], feedback: List[Feedback]=None):
        self.code = code
        self.feedback = feedback

    def generate_feedback(self, solution) -> None:
        sln = copy.deepcopy(solution)

        if self.code and solution.code and len(self.code) != len(solution.code):
            raise ValueError("Code is a different length than solution.")
        feedback = []
        for i, color in enumerate(self.code):
            if color == solution.code[i]:
                sln.code.remove(color)
                feedback.append(Feedback.RED)
        for i, color in enumerate(self.code):
            if color != solution.code[i] and color in sln.code:
                sln.code.remove(color)
                feedback.append(Feedback.WHITE)
        self.feedback = feedback


class Mastermind:
    def __init__(self, code: Code):
        self.code = code
        return


















@click.command("hello")
@click.version_option("0.1.0", prog_name="hello")
def play():
    click.echo("Hello World")

def main() -> int:
    """Echo the input arguments to standard output"""
    play()

if __name__ == '__main__':
    sys.exit(main())
