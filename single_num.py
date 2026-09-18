class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # oh yea this is using xor, pairs xor-ed w/ each other would cancel out

        if len(nums) == 1:
            return nums[0]
        
        start = nums[0]
        for i in range(1, len(nums)):
            start = start ^ nums[i]
        return start