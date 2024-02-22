# -*- coding: utf-8 -*-
from enum import Enum
from prompt_toolkit import HTML, print_formatted_text, prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from typing import List

import click
import copy
import random
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
        self.guesses = []
        self.num_total_colors = 6
        self.num_digits_in_code = 4
        self.num_turns_total = 11
        self.num_turns_left = self.num_turns_total
        self.colors = Color.aslist()[:self.num_total_colors]

    def generate_random_answer_code(self):
        self.answer_code_lst = []
        for _ in range(self.num_digits_in_code):
            i = random.randrange(0, len(self.colors))
            self.answer_code_lst.append(self.colors[i])
        self.answer_code = Code(self.answer_code_lst)

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
        """ Return randomized feedback. Assumes guess was already validated. """
        color_lst = self.user_input_to_colors(guess.split())
        guess = Code(code=color_lst)
        guess.generate_feedback(self.answer_code)
        self.guesses.append(guess)
        self.num_turns_left -= 1

        shuffled_feedback = copy.deepcopy(guess.feedback)
        random.shuffle(shuffled_feedback)
        return shuffled_feedback


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
        user_input = user_input.lower().strip()

        if user_input == "y":
            game = Mastermind()
            game.generate_random_answer_code()

            print_formatted_text(HTML(skyblue(f"Generating code using {game.num_digits_in_code} out of {game.num_total_colors} colors.")))
            print_formatted_text(HTML(skyblue(f"Here are the possible colors: ")))
            print_formatted_text(HTML(white("white, ") + blue("blue, ") + seagreen("green, ") + yellow("yellow, ") + red("red, ") + violet("violet.")))
            print_formatted_text(HTML(skyblue(f"\nPlease make your first guess by listing four colors (repeats okay),\nseparated by spaces.")))

            playing_game = True
            while playing_game:

                game_user_input = prompt(f"Turn {game.num_turns_total - game.num_turns_left + 1} > ", 
                    history=FileHistory('history.txt'),
                    auto_suggest=AutoSuggestFromHistory()
                )
                if game.is_valid_guess(game_user_input):
                    feedback = game.make_guess(game_user_input)
                    # check winning condition
                    if feedback == [Feedback.RED] * game.num_digits_in_code:
                        playing_game = False
                        print_formatted_text(HTML(seagreen("Hey! Congratulations! You did it! You won!!!!!")))
                    else:
                        formatted_feedback = [red("RED") if x == Feedback.RED else white("WHITE") for x in feedback]
                        print_formatted_text(HTML(skyblue("Feedback: ") + (" ".join(formatted_feedback) if formatted_feedback else yellow("None :("))))
                else:
                    print_formatted_text(HTML(red(f"I'm sorry, I couldn't parse that. Please make your guess again.")))

                if game.num_turns_left == 0:
                    playing_game = False  # lost.
                    print_formatted_text(HTML(red(f"I'm very sorry to tell you this, but you have in fact lost.\n The answer was {game.answer_code}. Try again?")))



        if user_input == "n":
            print_formatted_text(HTML(violet("Well. I'm not sure how to help you then. Are you having a nice day?")))
            chat_user_input = prompt('> ')
            print_formatted_text(HTML(violet("Good for you.\n")))


def main() -> int:
    """Echo the input arguments to standard output"""
    play()

if __name__ == '__main__':
    sys.exit(main())
