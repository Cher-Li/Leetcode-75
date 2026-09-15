class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        # so the subsequence has the same order of characters after deleting characters from the first
        # * dp prob, dp[i][j] rep LCS of text1[0...i] and text2[0...j] 
        # base case 0's just 0, 11 only if text1 == text2, and so on? 
        # also like, LCS can only ever be as long as the shorter of the two texts? 
        # n = len(text1) if len(text1) < len(text2) else len(text2)
        # ok that doesn't work b/c part of the subsequence could be after n
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)] # * init w/ zeroes

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]: # * 
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n] 