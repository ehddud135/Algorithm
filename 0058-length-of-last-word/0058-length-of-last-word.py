class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        print(s)
        split_result = s.split()
        print(split_result)
        last_word = len(split_result) - 1
        print(last_word)

        return len(split_result[last_word])
        """
        :type s: str
        :rtype: int
        """
        