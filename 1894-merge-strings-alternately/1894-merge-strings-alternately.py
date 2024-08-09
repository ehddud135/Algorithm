class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        n = min(len(word1), len(word2))
        for i in range(n):
            result += word1[i] + word2[i]
        if n < len(word1):
            result += word1[n:]
        elif n < len(word2):
            result += word2[n:]
        return result
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        