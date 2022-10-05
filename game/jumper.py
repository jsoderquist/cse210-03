import random

class Jumper:
    """The person hiding from the Seeker. 
    
    The responsibility of Hider is to keep track of its location and distance from the seeker. 
    
    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        word_list = ["apple","banana","pear","peach","mango","watermelon","strawberry"]
        self._word = random.choice(word_list)
        self._letters_guessed = []
        for i in range(len(self._word)): #add blank lines for each letter in the word
            self._letters_guessed.append("_")
        #parachute has an element for each line of the parachute
        self._parachute = ["  ___  ", " /___\ "," \   / ","  \ /  ","   O   ","  /|\  ","  / \  ","       ","^^^^^^^"]
    
    def get_parachute(self):
        """Gets a hint for the seeker.

        Args:
            self (Hider): An instance of Hider.
        
        Returns:
            string: A hint for the seeker.
        """
        parachute = ""
        for i in self._parachute: 
            parachute += i+"\n"
        return parachute

    def is_fallen(self):
        """Whether or not the hider has been found.

        Args:
            self (Hider): An instance of Hider.
            
        Returns:
            boolean: True if the hider was found; false if otherwise.
        """
        return (len(self._parachute) == 5)
        
    def check_guess(self, guess):
        """Watches the seeker by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """
        in_word = False
        if guess in self._word:
            in_word = True
        else:
            self._parachute.pop(0)
            if len(self._parachute) == 5: #show that you lost
                self._parachute[0] = "   x    "
        
        #update list of letters found
        for pos,char in enumerate(self._word):
            if(char == guess):
                self._letters_guessed[pos] = guess