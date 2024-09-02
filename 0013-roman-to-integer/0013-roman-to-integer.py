class Solution(object):
    def romanToInt(self, s):
        result = 0
        int_dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        n = len(s)
        for i in range(n):
            if i < n - 1 and int_dic[s[i]] < int_dic[s[i+1]]:
                result -= int_dic[s[i]]
            else:
                result += int_dic[s[i]]
        # print(result)

        return result

        """
        :type s: str
        :rtype: int
        """
        