class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # most straight forward is just, loop thr 0 to n, get number of 1's for each binary, append to ans
        # like for 5, 101, sum to be 2, and that becomes ans[5] 
        # is there some sort of relationship 
        # [0, 1, 1, 2, 1, 2, 2, 3, 1...] <- and keep going 
        # * hint of, divide into 2-3 = [1, 2], 4-7 = [1, 2, 2, 3], try to generate new range each time
        # and I know odd numbers always at least has the 1 in the 1's place

        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            # even nums: ans[2 * i] = ans[i]
            # odd nums: ans[2 * i + 1] = ans[i] + 1
            # if i % 2 == 0:
            #     ans[i] = ans[i // 2]
            # else:
            #     ans[i] = ans[i // 2] + 1

            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans 