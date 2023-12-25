import mask
import stack

class Wordle:
    def __init__(self, solution, possible_words):
        """
        Constructs Wordle object.
        :param solution: The correct word, a string.
        :param possible_words: List of many acceptable words.
        """
        self.solution = solution
        # Using stack object which will combine words and masks.
        self.word_stack = stack.Stack(possible_words)
        # Counting guesses.
        self.num_of_guesses = 0
        self.possible_words = possible_words

    def get_solution(self):
        """
        Returns solution.
        :return: Solution, string.
        """
        return self.solution

    def restart(self, solution=""):
        """
        Initialize the game to a new game, optionally accepts a solution (str) from its caller, and sets everything back to default values.
        If the function doesn't receive input then the solution should stay the same.
        :param solution:
        :return: No return
        """
        # Resets guesses
        self.num_of_guesses = 0
        # If solution is received, changes it.
        if not solution == "":
            self.solution = solution
        # Resets filtered stack.
        self.word_stack = stack.Stack(self.possible_words)

    def guess(self, word):
        """
        Handles a guess from the user (str) and return a mask object representing a feedback to the user based on his guess.
        Also makes sure the guess is in the allowed words dataset.
        :param word:
        :return: Mask of the word
        """
        word_mask = mask.Mask()
        # Uses compute_from func from object mask, which gets word and target (solution) and returns mask of word.
        word_mask = word_mask.compute_from(word,self.solution)
        # Filters stack with word and its mask.
        filtered_stack = self.word_stack.filter(self.solution,word_mask)
        # Adds guess count.
        print(word_mask.statuses)
        print(filtered_stack.words)
        self.num_of_guesses += 1
        return word_mask

    def lost_game(self):
        """
        Returns whether the game has been lost or not. Will be used after win check.
        :return: Bool. If lost True, otherwise False.
        """
        # If you didn't win on guess 6, you lost.
        if self.num_of_guesses == 6:
            return True


    def get_possible_words(self):
        """
        Returns all the possible words for guessing.
        :return: A list of words (strings)
        """
        return self.word_stack.get_words()