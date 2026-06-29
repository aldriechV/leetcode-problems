class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        score = 0
        for i in patterns:
            if i in word:
                score += 1
        return score