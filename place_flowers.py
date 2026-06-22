class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        # try to find some patterns: 
        # if there's an even number of adjacent 0's then max half of them
        # if odd, could do one more than half if not blocked either way

        # maybe something like "greedy" where you just directly place them in and if reach the end of the flowerbed without n = 0 then return false
        # can't do sliding window to find the longest window of 0's since can alternate

        # naive approach is just, actually go through and place down the flowers
        # for i in range(len(flowerbed)):
        #     # edge cases of first and last position
        #     if n >= 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 1 and flowerbed[i + 1] != 1: # <- limits cases of 0 on left? 
        #         flowerbed[i] = 1
        #         n = n - 1
        #     elif n == 0: 
        #         return True
        
        # return False

        # * lmao
        if n == 0:
            return True

        for i in range(len(flowerbed)): 
            # * deals w/ edges
            left_empty = (i == 0) or flowerbed[i - 1] == 0
            right_empty = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0

            if flowerbed[i] == 0 and left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1

            if n == 0:
                return True

        return False
        # O(N) time