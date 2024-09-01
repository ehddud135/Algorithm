class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
            print(nums)
        print(len(nums))
        return len(nums)
                
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        