import random

class Jumper:
    """The parachuter with a word to be guessed. 
    
    The responsibility of Jumper is to have a word and track what has been guessed
    
    Attributes:
        _word (string) - the chosen word 
        _letters_guessed (list[char]) - a list of the letters that have been guessed 
        _parachute (list[string]) - list of the pieces of the parachute that are left
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        word_list = ["apple","banana","pear","peach","mango","watermelon","strawberry"]
        self._word = random.choice(word_list)
        self._letters_guessed = []
        for i in range(len(self._word)): #add blank lines for each letter in the word
            self._letters_guessed.append("_")
        #parachute has an element for each line of the parachute
        self._parachute = ["  ___  ", " /___\ "," \   / ","  \ /  ","   O   ","  /|\  ","  / \  ","       ","^^^^^^^"]
    
    def get_parachute(self):
        """Gets a the parachute to be displayed.

        Args:
            self (Jumper): An instance of Jumper.
        
        Returns:
            list[string]: The parachute
        """
        parachute = ""
        for i in self._parachute: 
            parachute += i+"\n"
        return parachute

    def is_fallen(self):
        """Whether or not there's still parachute left.

        Args:
            self (jumper): An instance of jumper.
            
        Returns:
            boolean: True if the parachute is gone; false if otherwise.
        """
        return (len(self._parachute) == 5)
        
    def check_guess(self, guess):
        """Updates parachute and letters guessed based on the guessed letter.

        Args:
            self (Jumper): An instance of Jumper.
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