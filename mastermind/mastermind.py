# -*- coding: utf-8 -*-
from enum import Enum
from prompt_toolkit import prompt
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
    def __init__(self, answer_code: Code):
        self.answer_code = answer_code

    """
    MOST BASIC VERSION: what needs to happen every new game?

    - 4-color code randomly chosen
    - tell you which 6 colors are available to choose from 
    - prompt you for first guess
    - validate guess (used only valid colors w/ accepted name spelling, correct number of colors) with informative error messages
    - you get 11 guesses (can be repeats--that's your fault)
    - gives RANDOMIZED feedback for each guess
    - if guess is correct, end game as WIN
    - if 11th guess is still wrong, end game as LOSE and SHOW ANSWER
    
    gameplay options:
    - mid-game, you can give up and start a new game if you want
    - option for no double colors

    """
















@click.command("hello")
@click.version_option("0.1.0", prog_name="mastermind")  # TODO: replace version & name with setup.py version/name
def play():
    click.echo("Welcome to Mastermind! (exit with control-D)")
    while 1:
        user_input = prompt('>')
        print(user_input)

def main() -> int:
    """Echo the input arguments to standard output"""
    play()

if __name__ == '__main__':
    sys.exit(main())
