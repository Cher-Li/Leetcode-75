class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        # insert / delete until the letter frequency of the two word match, then just replace? I mean not quite since you can replace the same letter with different ones
        # is dp just, min number of operations convert word1 up to i to word2 up to j? 
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)] 
        # convert up to i - 1 and j - 1 instead
        # * base cases: dp[i][0] is i b/c i deletions, same w/ dp[0][j] w/ j
        for i in range(m + 1): # * + 1's
            dp[i][0] = i
        for j in range(n + 1): 
            dp[0][j] = j

        for i in range(1, m + 1): # * also + 1's, start from 1, basically shift 1 over
            for j in range(1, n + 1):
                # try to update dp 
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] 
                
                # * otherwise should be min of, replace word1 with word2 char, delete char, or vice versa
                else: 
                    # replace, delete, insertion respectively
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1 
        
        return dp[m][n]