class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # dp style problem
        # at bottom right, had to have come from tile above, or tile to the left
        # base cases are tiles straight down or across since only move down or right, dp = 1
        dp = [[1] * n for _ in range(m)] 
        for i in range(1, m):
            for j in range(1, n):
                # keep updating each new tile
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1] 