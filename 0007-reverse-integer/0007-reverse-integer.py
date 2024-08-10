class Solution(object):
    def reverse(self, x):
        result = 0
        y = x
        if x < 0:
            y = x * -1 
        while y != 0:
            result = result * 10 + y % 10
            y = y / 10
            y = int(y)
        if x < 0:
            result = result * -1
        if result > 2147483647 or result < -2147483647:
            result = 0

        return int(result)
        """
        :type x: int
        :rtype: int
        """
        