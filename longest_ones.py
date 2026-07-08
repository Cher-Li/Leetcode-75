class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # sliding window vibes? 
        # like, keep a frame of 1s, about to have at most k 0s within that frame, and just keep incrementing until the end
        start = end = 0
        num_zeroes = 0
        # max_ones = cur_ones = 0
        answer = 0

        # * oh, count max num 1s *after* flipping the 0s so it's just the length of the window
        
        # while end < len(nums):
        #     # like, can increment end to a 0 is num_zeroes less than k 
        #     end += 1
        # * the above possible out of bound

        for right in range(len(nums)): 
            # if nums[end] == 1:
            #     cur_ones += 1
            if nums[right] == 0:
                num_zeroes += 1

            # elif nums[end] == 0:
            #     # two cases of whether num_zeroes exceeds? 
            #     num_zeroes += 1
            #     if num_zeroes > k: 
            #         # increment start past the first zero and subtract any ones along the way? 
                
            # max_ones = max(cur_ones, max_ones) 

            while num_zeroes > k: 
                if nums[start] == 0:
                    num_zeroes -= 1

                start += 1
        
            answer = max(answer, right - start + 1) # * just need the length of that window
        
        return answer