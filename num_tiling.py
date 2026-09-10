class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10 ** 9 + 7

        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        
        # if 2 tiles, use 1 domino tile, if 2 tiles and one attached, 1 tromino tile
        # like for 2 x 2, can't use tromino, it has to be groups of 3 interlocking? 

        # # * dp[i] = number of ways to fully tile 2 x i board
        # dp[0] = 1 # * 
        # dp[1] = 1
        # dp[2] = 2 # domino horizontal vs vertical
        # # dp[3] = 5 # first ex

        # for i in range(3, n + 1):
        #     dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % mod
        
        # return dp[n]

        # * space optimizing
        p3, p2, p1 = 1, 1, 2 # dp[i - 1] to dp[i - 3]
        for i in range(3, n + 1):
            current = (p1 * 2 + p3) % mod 
            p3, p2, p1 = p2, p1, current # shift this way so current is newest
        
        return p1