class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bottom up approach, keep track of only last 3 numbers
        if n == 0:
            return 0
        if n <= 2:
            return 1

        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c # * just keep shifting the three nums incrementally 

        return c

# class Solution(object):
#     def __init__(self):
#         self.dp = {} 

#     def tribonacci(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
        
#         # dp = [-1] 
#         # dp[0] = 0
#         # dp[1] = dp[2] = 1

#         if n == 0 or n == 1:
#             return n
#         elif n == 2:
#             return 1

#         if n not in self.dp:
#             self.dp[n] = (
#                 self.tribonacci(n - 1)
#                 + self.tribonacci(n - 2)
#                 + self.tribonacci(n - 3)
#             )

#         return self.dp[n]

#         # else:
#         #     # somehow incorporate dp so it doesn't repeatedly calculate each subproblem? 
#         #     if dp[n - 1] == -1:
#         #         dp[n - 1] = self.tribonacci(n - 1)
#         #     elif dp[n - 2] == -1:
#         #         dp[n - 2] = self.tribonacci(n - 2)
#         #     elif dp[n - 3] == -1:
#         #         dp[n - 3] = self.tribonacci(n - 3)

#         #     dp[n] = dp[n - 1] + dp[n - 2] + dp[n - 3]
#         #     return dp[n]

#         #     # return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3) 