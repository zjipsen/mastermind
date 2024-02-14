# -*- coding: utf-8 -*-
from enum import Enum
from prompt_toolkit import HTML, print_formatted_text, prompt
from typing import List

import click
import copy
import sys


class Feedback(Enum):
    WHITE = 1
    RED = 2


class Color(Enum):
    BLUE = 1
    GREEN = 2
    VIOLET = 3
    WHITE = 4
    YELLOW = 5
    RED = 6

    @classmethod
    def aslist(cls):
        return [cls.BLUE, cls.GREEN, cls.VIOLET, cls.WHITE, cls.YELLOW, cls.RED]


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
        self.num_total_colors = 6
        self.num_digits_in_code = 4
        self.num_turns = 11

    def generate_random_answer_code(self):
        pass

    def user_input_to_colors(self, guess):
        # Takes in a list of strings and attempts to map each string to a known Color
        converted_guess = []
        for color in [g.lower() for g in guess]:
            if color == "blue" or color == "b":
                converted_guess.append(Color.BLUE)
            elif color == "green" or color == "g":
                converted_guess.append(Color.GREEN)
            elif color == "violet" or color == "v":
                converted_guess.append(Color.VIOLET)
            elif color == "white" or color == "w":
                converted_guess.append(Color.WHITE)
            elif color == "yellow" or color == "y":
                converted_guess.append(Color.YELLOW)
            elif color == "red" or color == "r":
                converted_guess.append(Color.RED)
        return converted_guess

    def is_valid_guess(self, guess) -> bool:
        guess_lst = guess.split()
        if len(guess_lst) != self.num_digits_in_code:  # guess must be number of digits long
            return False

        color_lst = self.user_input_to_colors(guess_lst)
        if len(guess_lst) != len(color_lst):  # something went wrong in conversion
            return False
        return True

    def make_guess(self, guess) -> List[Feedback]:
        #  assuming guess was already validated
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

    # loop until user exits with control-D
    while 1:
        print_formatted_text(HTML(skyblue('Would you like to start a new game? (y/n)')))
        user_input = prompt('> ')

        if user_input.lower() == "y":
            game = Mastermind()

            print_formatted_text(HTML(skyblue(f"Generating code using {game.num_digits_in_code} out of {game.num_total_colors} colors.")))
            print_formatted_text(HTML(skyblue(f"Here are the possible colors: ")))
            print_formatted_text(HTML(white("white, ") + blue("blue, ") + seagreen("green, ") + yellow("yellow, ") + red("red, ") + violet("violet.")))
            print_formatted_text(HTML(skyblue(f"\nPlease make your first guess by listing four colors (repeats okay), separated by spaces.")))

            playing_game = True
            while playing_game:

                user_input = prompt('> ')
                if game.is_valid_guess(user_input):
                    feedback = game.make_guess(user_input)
                else:
                    pass # re-get user input until it's valid


        if user_input == "n":
            print_formatted_text(HTML(violet("Well. I'm not sure how to help you then. Are you having a nice day?")))
            user_input = prompt('> ')
            print_formatted_text("++" + user_input)


def main() -> int:
    """Echo the input arguments to standard output"""
    play()

if __name__ == '__main__':
    sys.exit(main())
