class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # straightforward soln just manually keep track of the first three elmts and compare, increment all by 1 until the last one reaches the end then return false <- nope not quite, need a bigger sliding window
        # could keep one as reference then loop over combinations of future two elmts, both has to be greater than reference in ascending order <- N^3 tho? 

        # focus on smallest number at the "start" and the next smallest num
        # always want the smallest starting num
        # if in between two nums, set it to the second num
        # and if > the previous two, return true

        # O(N) time, O(1) space

        # first = nums[0] # or also set to inf at start
        first = float('inf')
        second = float('inf') # *
        # for i in range(len(nums)):
        #     if nums[i] <= first:
        #         first = nums[i]
        #     # elif nums[i] > first and nums[i] <= second: # * mutually exclusive
        #         # * also technically don't need this first part? 
        #     elif nums[i] <= second:
        #         second = nums[i]
        #     else:
        #         return True

        for num in nums: # w/o indexing to see if faster
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False