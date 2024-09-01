class Solution(object):
    def addBinary(self, a, b):
        a1 = int(a, 2)
        b1 = int(b, 2)
        result = a1 + b1
        result = bin(result)[2:]
        return str(result)
        
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        