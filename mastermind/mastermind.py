# -*- coding: utf-8 -*-
from enum import Enum
from prompt_toolkit import HTML, print_formatted_text, prompt
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
    def __init__(self, answer_code: Code=None):
        self.answer_code = answer_code

    def generate_random_answer_code(self):
        pass

    def is_valid_guess(self, guess) -> bool:
        pass

    def make_guess(self, guess) -> List[Feedback]:
        pass


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


def skyblue(text):
    return f'<skyblue>{text}</skyblue>'

def blue(text):
    return f'<deepskyblue>{text}</deepskyblue>'

def seagreen(text):
    return f'<seagreen>{text}</seagreen>'

def violet(text):
    return f'<violet>{text}</violet>'

def white(text):
    return f'<white>{text}</white>'

def yellow(text):
    return f'<gold>{text}</gold>'

def red(text):
    return f'<indianred>{text}</indianred>'


@click.command("hello")
@click.version_option("0.1.0", prog_name="mastermind")  # TODO: replace version & name with setup.py version/name
def play():
    click.echo("Welcome to Mastermind! (exit with control-D)")
    num_total_colors = 6
    num_colors = 4
    num_turns = 11

    # loop until user exits with control-D
    while 1:
        print_formatted_text(HTML(skyblue('Would you like to start a new game? (y/n)')))
        user_input = prompt('>')

        if user_input.lower() == "y":
            print_formatted_text(HTML(skyblue(f"Generating code using {num_colors} out of {num_total_colors} colors.")))
            print_formatted_text(HTML(skyblue(f"Here are the possible colors: ")))
            print_formatted_text(HTML(white("white, ") + blue("blue, ") + seagreen("green, ") + yellow("yellow, ") + red("red, ") + violet("violet.")))

            print_formatted_text(HTML(skyblue(f"\nPlease make your first guess by listing four colors (repeats okay), separated by spaces.")))

            playing_game = True
            while playing_game:
                game = Mastermind()

                user_input = prompt('>')
                if game.is_valid_guess(user_input):
                    feedback = game.make_guess(user_input)
                else:
                    pass # re-get user input until it's valid


        if user_input == "n":
            print_formatted_text(HTML(violet("Well. I'm not sure how to help you then. Are you having a nice day?")))
            user_input = prompt('>')
            print_formatted_text("++" + user_input)



def main() -> int:
    """Echo the input arguments to standard output"""
    play()

if __name__ == '__main__':
    sys.exit(main())
