# mastermind
play the game mastermind with command line visualization.

Install requirements:

	> pip3 install -r requirements.txt

Run tests:

	> python3 tests/tests.py 

Begin game:

	> python3 mastermind/mastermind.py


    Version 1 completed. The code now has:

    - 4-color code randomly chosen
    - tell you which 6 colors are available to choose from 
    - prompt you for first guess
    - validate guess (used only valid colors w/ accepted name spelling, correct number of colors) with informative error messages
    - you get 11 guesses (can be repeats--that's your fault)
    - gives RANDOMIZED feedback for each guess
    - if guess is correct, end game as WIN
    - if 11th guess is still wrong, end game as LOSE and SHOW ANSWER
    
    Next step:
    - refactor so computer can play without going through human user/CLI code
    - create an algorithm for the computer to play as the guesser
    - CLI shows colors while typing
    
    Future gameplay options:
    - mid-game, you can give up and start a new game if you want
    - option for no double colors
