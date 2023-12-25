import mask
class Stack:
    def __init__(self, words):
        """
        Constructs a Stack, list of word which can be combined with masks.
        :param words: A list of words, strings.
        """
        self.words = words

    """ def filter(self, word, mask):
        
        Given a target word and a mask, filters all words in the stack that does not fit to the mask.
        :param word: A target word.
        :param mask: A masked list, related to the word.
        :return: No return
        
        # Used to delete all words.
        words_to_remove = []
        # Letters that did not appear in mask.
        black_letters = []
        # Goes through entire word
        for i in range(len(word)):
            # Letter does not appear in solution (0 in mask).
            if mask.statuses[i] == 0:
                black_letters.append(word[i])
            # Exact position
            if mask.statuses[i] == 2:
                for optional_word in self.words:
                    # Removes words that do not contain letter in exact position.
                    if optional_word[i] != word[i]:
                        words_to_remove.append(optional_word)
        # Removes words that contain blacked letters.
        for optional_word in self.words:
            for b_letter in black_letters:
                if b_letter in optional_word:
                    words_to_remove.append(optional_word)
        # The actual removal.
        for word_tr in words_to_remove:
            if word_tr in self.words:
                self.words.remove(word_tr)

        return self
"""

    def get_words(self):
        """
        Returns a list of the words in the stack.
        :return: List of words (strings).
        """
        return self.words

    def __len__(self):
        """
        Returns length of the stack
        :return: length, int.
        """
        return len(self.words)

    def __iter__(self):
        """
        Creates and returns an iterator of the stack
        :return: Iterator (iter object) of strings.
        """
        return iter(self.words)


    def filter(self, word, mask):
        """
        Given a target word and a mask, filters all words in the stack that does not fit to the mask.
        :param word: A target word.
        :param mask: A masked list, related to the word.
        :return: No return
        """
        # Used to delete all words.
        words_to_remove = []
        # Letters that did not appear in mask.
        letters = []
        # Goes through entire word
        for i in range(5):
            letters.append(word[i])
        for i in range(len(word)):
            # If letter is
            if mask.statuses[i] == 0:
                for optional_word in self.words:
                    if optional_word[i] in word and optional_word.count(optional_word[i]) < 2:
                            print(optional_word + "removed 0")
                            words_to_remove.append(optional_word)

            if mask.statuses[i] == 1:
                for optional_word in self.words:
                    if word[i] == optional_word[i] or optional_word[i] not in letters:
                        print(letters)
                        print(optional_word+" removed 1" )
                        words_to_remove.append(optional_word)
            # Exact position
            if mask.statuses[i] == 2:
                for optional_word in self.words:
                    # Removes words that do not contain letter in exact position.
                    if optional_word[i] != word[i]:
                        print(optional_word+" removed 2")
                        words_to_remove.append(optional_word)
        # Removes words that contain blacked letters.
        # The actual removal.
        for word_tr in words_to_remove:
            if word_tr in self.words:
                self.words.remove(word_tr)

        return self