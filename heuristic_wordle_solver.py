import mask
import stack
from itertools import product
import statistics
import copy

# Generate all 5-numbered lists of combinations
mask_combinations = list(product((0,1,2), repeat=5))

class HeuristicWordleSolver:

    def __init__(self, game):
        """
        Construct a wordle solver object.
        :param game: A wordle object
        """
        self.game = game
        self.word_stack = stack.Stack(game.get_possible_words())
        self.num_of_guesses = 0
    def choose_word(self):
        """
        Chooses the word that minimizes the stack of the remaining relevant words.
        Only for the first guess in the game returns the word "crane" because of computation time.
        :return:
        """
        global mask_combinations
        chosen_word = ""
        words_grades = []
        words = []
        # First guest is "crane".
        if self.game.num_of_guesses == 0:
            chosen_word = "crane"
        else:
            words_tocheck = copy.deepcopy(self.game.word_stack.get_words())
            for i in range(len(words_tocheck)):
                try:
                    tmp_word = words_tocheck[i]
                except:
                    break
                stacks_of_word = []
                # For each possible mask, appends stack for the word.
                for m in mask_combinations:
                    new_stack = copy.deepcopy(self.word_stack)
                    new_mask = mask.Mask(m[0],m[1],m[2],m[3],m[4])
                    new_stack.filter(tmp_word, new_mask)
                    stacks_of_word.append(new_stack)
                stack_lens = []
                # Sums all stack lengths of a word and all possible masks.
                for stck in stacks_of_word:
                    stack_lens.append(len(stck))
                # Calculates variance of all sizes of all words
                words_grades.append(statistics.variance(stack_lens))
                words.append(tmp_word)
            # Gets minimal variance value index
            minpos = words_grades.index(min(words_grades))
            # Chooses word by minimal variance of lengths of stacks.
            chosen_word = words[minpos]
        return chosen_word


    def play_step(self):
        """
        Play a single step in the game. Guesses a word based on the stack minimization principle
        :return: No return
        """
        # Makes a guess, based on choosing func.
        guess_word = self.choose_word()
        mask = self.game.guess(guess_word)
        self.word_stack.filter(guess_word,mask)
        self.num_of_guesses += 1
        if self.won_game():
            print("won")
        elif self.lost_game():
            print("lost")

    def won_game(self):
        """
        Returns whether the game has been won or not.
        :return: Bool. If won True, otherwise False
        """
        # If only 1 left in filter
        if len(self.word_stack) == 1:
            return True
        return False

    def lost_game(self):
        """
        Returns whether the game has been lost or not.
        :return: Bool. If lost True, otherwise False
        """
        if self.num_of_guesses == 6:
            return True
        else:
            return False