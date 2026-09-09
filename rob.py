class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # so could either, get current house value, skip the next, or skip the current and get next house value
        # from the end it's either, from n - 1, or from n - 2? 

        if not nums:
            return 0

        dp = [0] * (len(nums) + 1) # max val considering first i houses
        # * base cases
        dp[0] = 0
        dp[1] = nums[0] 

        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
            # either skip this house and keep all previous dp[i]
            # or get this value and the dp from 2 houses ago
        
        return dp[len(nums)] # or dp[-1] 

        # # less space complexity: 
        # # rob1 = max money from 2 houses ago
        # # rob2 = max money from 1 house ago
        # rob1, rob2 = 0, 0
        
        # for n in nums:
        #     # rob vs skip each house
        #     current_max = max(n + rob1, rob2)
        #     rob1 = rob2
        #     rob2 = current_max
            
        # return rob2