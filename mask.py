class Mask:
    def __init__(self, n1=0, n2=0, n3=0, n4=0, n5=0):
        """
        Constructs mask
        :param n1: first number
        :param n2: second number
        :param n3: third number
        :param n4: forth number
        :param n5: fifth number
        """
        # An array of numbers representing letter statuses in mask
        self.statuses = []
        self.statuses.append(n1)
        self.statuses.append(n2)
        self.statuses.append(n3)
        self.statuses.append(n4)
        self.statuses.append(n5)

    def get_statuses(self):
        """
        Returns statuses of each letter.
        :return: statuses, list of ints.
        """
        return self.statuses

    def change_status(self,i,status):
        """
        Changes status of masking of a specific letter.
        :param i: Letter index
        :param status: New status
        :return: No return
        """
        self.statuses[i] = status

    @staticmethod
    def compute_from(word,target):
        """
        A static method. Computes mask describing a given word, given a target word.
        :param word: A suggested word, string.
        :param target: The correct word, which we will compare "word" to. String.
        :return: Mask object. The statuses of each letter.
        """
        mask = Mask()
        # Used in case a letter appears in word more than in target.
        already_identified = []
        # Checks every letter in word.
        for i in range(len(word)):
            if word[i] in target:
                # Letter exists in target.
                if word[i] == target[i]:
                    # Exact location.
                    mask.change_status(i,2)
                # Not Exact location. And we want to check if it appeared before.
                elif word[i] not in already_identified:
                    mask.change_status(i,1)
                # If letter appears in word more than in target, we want to avoid coloring it yellow in second appearance.
                if word.count(word[i]) > target.count(word[i]):
                    already_identified.append(word[i])
        # If 4 greens and 1 yellow (it may be a letter that appears twice in word -> colored yellow), we want to remove yellow-color.
        if mask.statuses.count(2) == 4 and 1 in mask.statuses:
            mask.change_status(mask.statuses.index(1),0)
        return mask


