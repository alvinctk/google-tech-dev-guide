import random
from collections import defaultdict
class Hangman:
    """
    Hangman class
    """
    def __init__(self, all_secret_word, number_of_guess):

        # To store number of guess allowed for the game
        self.number_of_guess = number_of_guess

        # To used to determine whether to print user's previous guesses
        self.start = number_of_guess

        # To store the final word to be shown
        self.random_word = random.choice(all_secret_word).lower()

        # To store user's previous guesses
        self.user_guess = set()

        # To used in determing which characters are incorrect
        self.fill_in_blank = "_"

        # Build guess word from secret word
        self.guess_word = [self.fill_in_blank] * len(self.random_word)

        # Preprocess the secret word to store the indices for a faster search
        self.secret_word = defaultdict(list)
        for i, character in enumerate(self.random_word):
            self.secret_word[character].append(i)

    def show_number_of_guess(self):
        """
        Show the user the current hangman word
        Show the user number of guesses left
        Show the user the previous character attempts
        """
        # Show the current hangman word
        user_guess_word = " ".join(self.guess_word)
        print("The word now looks like this: {}".format(user_guess_word))

        # To inform user the number of guess left
        if self.number_of_guess == 1:
            print("You have only one guess left")

        elif self.number_of_guess:
            print("You have {} guesses left.".format(self.number_of_guess))

        # Show user's previous guesses
        if self.start != self.number_of_guess:
            print("Your previous guesses are {}".format(self.user_guess))

    def is_missing_letters(self):
        """
        Returns True if there are still missing letters in the hangman word.
        Otherwise, returns False.

        Prints result if according to missing letters and number of guesses
        """
        # To determine whether there are missing letters in hangman word
        blank, guess_word = self.fill_in_blank, self.guess_word
        missing_letters = any(filter(lambda x: x == blank, guess_word))

        # Print result
        if not missing_letters:
            print("You win")

        elif self.number_of_guess == 0:
            print("You are completely hung.")
            print("The word was: {}".format(self.random_word))
            print("You lose")

        return missing_letters

    def ask_question(self):
        """
        Ask the user for an input guess
        Returns a lowercase input strip of leading and trailing whitespaces
        """
        print("Your guess: ", end="")
        return input().strip().lower()

    def update_guess_word(self):
        """
        Update user guess to the hangman word
        """

        # Retrieve user input
        c = self.ask_question()
        self.user_guess.add(c)

        # If the character exists in the preprocess indicies dictionary
        if c in self.secret_word and len(self.secret_word[c]) > 0:

            # Set guess word
            index = self.secret_word[c][0]
            self.guess_word[index] = c
            self.secret_word[c] = self.secret_word[c][1:]
            print("That guess is correct")
        else:
            print("There are no {}'s in the word".format(c))

        # Update the number of guesses
        self.number_of_guess -= 1

    def play_game(self):
        """
        Play the hangman game
        """
        print("Welcome to Hangman!")

        # Main program loop to keep asking the user until game is won
        # or game is lost
        while self.is_missing_letters() and self.number_of_guess:
            self.show_number_of_guess()
            self.update_guess_word()
            print()

if __name__ == "__main__":
    # For testing a simple case
    #words = ["buoy"]

    words =  ["BUOY", "COMPUTER", "CONNOISSEUR", "DEHYDRATE", "FUZZY",
              "HUBBUB", "KEYHOLE", "QUAGMIRE", "SLITHER", "ZIRCON"]

    # Plays the hangman game in the terminal
    hangman_game = Hangman(all_secret_word=words, number_of_guess=8)
    hangman_game.play_game()
