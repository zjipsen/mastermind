# mastermind
Play the game mastermind with command line visualization.

Install requirements:

	> pip3 install -r requirements.txt

Run tests:

	> python3 tests/tests.py

Begin game:

	> python3 mastermind/mastermind.py


    Version 1 completed. The game includes:

    - 4-color code randomly chosen as the answer code, which the player should try to guess
    - tell player which 6 colors are available to choose from 
    - prompt player for first guess
    - validate guess (used only valid colors w/ accepted name spelling, correct number of colors) with informative error messages
    - player gets 11 guesses (can be repeats)
    - gives RANDOMIZED feedback for each guess
    - if guess is correct, end game as WIN
    - if 11th guess is still wrong, end game as LOSE and SHOW ANSWER

    Next steps:
    - refactor so computer can play without going through human user/CLI code
    - design an algorithm for the computer to play as the guesser
    - CLI shows colors while user is typing
    
    Future gameplay options:
    - mid-game, you can give up and start a new game if you want
    - option for no double colors
