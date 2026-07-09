class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # isn't this similar to max consec ones with k = 1? 
        # and so the final answer would be the length of the window - 1? 

        start = end = 0
        num_zeroes = 0
        answer = 0

        for right in range(len(nums)): 
            if nums[right] == 0:
                num_zeroes += 1

            while num_zeroes > 1: 
                if nums[start] == 0:
                    num_zeroes -= 1

                start += 1
        
            answer = max(answer, right - start) # no + 1 b/c it's length - 1?  

            # yea since (window length) - 1 = (right - start + 1) - 1 = right - start
        return answer
        # O(N) time and O(1) space