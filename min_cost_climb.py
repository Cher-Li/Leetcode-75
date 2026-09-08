class Solution(object):
    def minCostClimbingStairs(self, cost):
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2]) # just track 2 var
        
        return min(cost[-1], cost[-2])

# last soln a bit better runtime wise compared to the below
# class Solution(object):
#     def minCostClimbingStairs(self, cost):
#         n = len(cost)
#         # min cost to reach the ith step instead of cost to top from ith
#         dp = [0] * (n + 1)
        
#         for i in range(2, n + 1):
#             dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            
#         return dp[n]

# class Solution(object):
#     def minCostClimbingStairs(self, cost):
#         """
#         :type cost: List[int]
#         :rtype: int
#         """
        
#         # dp prob, from top of staircase, cost is either cost of prev step + 1, or cost of prev prev step + 2? 
#         # like, fill up dp[len(cost)] 
#         # oh, dp[i] is cost to climb to top starting from ith staircase? 

#         n = len(cost)
#         dp = [0] * (n + 2) # * dp[n] and dp[n + 1] are base cases
#         # dp[n] = 0 

#         for i in range(n - 1, -1, -1):
#             # loop back to 0
#             dp[i] = cost[i] + min(dp[i + 1], dp[i + 2]) 
        
#         return min(dp[0], dp[1]) # * start at step 0 or 1