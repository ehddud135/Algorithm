class Solution(object):
    def searchInsert(self, nums, target):
        result = 0
        for i in range(len(nums)):
            if nums[i] >= target:
                print(i)
                result = i
                break
            else:
                result = len(nums)
        return result
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        