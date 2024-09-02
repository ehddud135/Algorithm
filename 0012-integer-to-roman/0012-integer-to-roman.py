class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        roman_dic = {
            1000 : 'M',
            900 : 'CM',
            500 : 'D',
            400 : 'CD',
            100 : 'C',
            90 : 'XC',
            50 : 'L',
            40 : 'XL',
            10 : 'X',
            9 : 'IX',
            5 : 'V',
            4 : 'IV',
            1 : 'I'
        }
        for i in roman_dic.keys():
            print(i)
            while num >= i:
                num -= i
                result += roman_dic[i]
        return result

        """
        :type num: int
        :rtype: str
        """
        