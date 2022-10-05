class Guesser:
    """The person looking for the Hider. 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
    """

    def __init__(self):
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """

        self.guess = 'a'
       
    def get_guess(self):
        """Gets the current location.
        
        Returns:
            number: The current location,
        """

        return self._guess
        
    def change_guess(self, guess):
        """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """

        self._guess = guess