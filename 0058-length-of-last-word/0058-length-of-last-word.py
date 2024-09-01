class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        print(s)
        split_result = s.split()
        print(split_result)
        result = len(split_result)
        print(result)

        return len(split_result[result-1])
        """
        :type s: str
        :rtype: int
        """
        