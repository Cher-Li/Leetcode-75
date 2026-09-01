class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # greater than neighbors so, naive solution is just to loop through all nums and check if greater than both left and righthand side
        # maybe something about arrays to keep track of bool of true or not? 
        # O(log n) time so something to do with halving the search each time? 
        # ok yea so sorta slope vibes, keep going up the slope until it's a peak

        left = 0
        right = len(nums) - 1
        # while left <= right:
        while left < right: 
            mid = (right + left) // 2
            # if nums[left] < nums[right]: 
                # left to right downward slope? Move right to mid? 

            # * well want to check middle elmt and the left vs right neighbors? 
            if nums[mid] < nums[mid + 1]:
                # left to right upward slope
                left = mid + 1
            else: 
                # peak at mid or leftwards
                right = mid
        
        return left