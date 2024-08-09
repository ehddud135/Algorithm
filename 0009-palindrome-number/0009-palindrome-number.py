class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            result = bool(True)
        else:
            result = bool(False)
        return result
        """
        :type x: int
        :rtype: bool
        """
        