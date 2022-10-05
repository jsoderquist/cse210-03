# cse210-03
Jumper Game

This game is just like the game "Hang Man." A word is randomly chosen, and blanks are displayed for every letter in the word. The player has to guess the word one letter at a time. As wrong letters are guessed, the "jumper" loses more of his parachute. If the jumper loses all of his parachute, the game is over, and if the player guesses all the letters in the word, the game is over.

Begin the game from the __main__.py file

Design:

Director: 
Attributes: _jumper - a parachuter who has a letter to be guessed
_is_playing - determines whether the game is still going
_guesser - gets information from the player
_terminal_service - displays to the terminal
Behaviors: start_game - starts the game
_get_inputs - gets input from the player
_do_updates - determine what to do with the inputs
_do_outputs - displays what happened

Guesser:
Attributes: _guess - the player's guess
Behaviors: get_guess - allows other classes to know the guess
change_guess - takes a new guess from the player

Jumper:
Attributes: _word - the chosen word
_letters_guessed - a list of the letters that have been guessed
_parachute - list of the pieces of the parachute that are left
Behaviors: get_parachute - lets the parachute be accessed and displayed
is_fallen - determines whether the parachute is gone
check_guess - updates based on the guessed letter

TerminalService:
Attributes: none
Behaviors: read_letter - gets a new letter from the user
write_text - writes to the terminal
