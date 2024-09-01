class Solution(object):
    def plusOne(self, digits):
        append = 0
        last_num = len(digits) - 1
        digits[last_num] = digits[last_num] + 1
        for i in range(last_num, -1, -1):
            print(i)
            print(digits)
            if digits[i] == 10:
                if i == 0:
                    digits[0] = 1
                    append = 1
                else:
                    digits[i-1] = digits[i-1] + 1
                    digits[i] = 0
                print(digits)
            elif digits[i] != 10:
                break
                print(digits)
        print(digits)
        if append == 1:
            digits.append(0)
        return digits
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        