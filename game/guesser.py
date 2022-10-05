class Guesser:
    """The player. 
    
    The guesser keeps track of what the player has input
    
    Attributes:
        guess (char): The player's last guessed letter.
    """

    def __init__(self):
        """Constructs a new Guesser.

        Args:
            self (Guesser): An instance of Guesser.
        """

        self._guess = 'a'
       
    def get_guess(self):
        """Gets the last guess.
        
        Returns:
            character: the last guessed letter,
        """

        return self._guess
        
    def change_guess(self, guess):
        """Changes the guess to a new guess.

        Args:
            self (Guesser): An instance of Guesser.
            guess (char): The guessed letter.
        """

        self._guess = guess