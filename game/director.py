from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.guesser import Guesser


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._guesser = Guesser()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._do_outputs()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        new_guess = self._terminal_service.read_letter("Guess a letter [a-z]: ")
        self._guesser.change_guess(new_guess)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        guess = self._guesser.get_guess()
        self._jumper.check_guess(guess)
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        word_list = self._jumper._letters_guessed
        display_word = "\n"
        for i in word_list:
            display_word += i
        display_word += "\n"
        self._terminal_service.write_text(display_word) #show letters guessed so far
        display_parachute = self._jumper.get_parachute()
        self._terminal_service.write_text(display_parachute) #show the jumper
        if self._jumper.is_fallen():
            self._is_playing = False
        if "_" not in display_word:  #end the game if they win
            self._is_playing = False