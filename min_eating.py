# import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        # if h matches the number of piles, need to eat a pile per hour so output the max num
        # otherwise can sorta, split up bigger piles into multiple k's? 
        # probably sort piles min to max, and just keep decrementing from largest if able to? 

        # search space for k, abs minimum is 1, abs max is max pile
        # and find the limit in which eat all bananas within that many hours
        # * left and right not 0 and len(pile) but k itself
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            # if self.helper(piles, h, mid) != 1: # return 1 if viable?
            if not self.helper(piles, h, mid): # or bool directly
                left = mid + 1
            else:
                right = mid

        return left

    # instead of doing it naively and simulating the whole thing, calc how many hours it takes to eat all at that speed and only then compare to h
    def helper(self, piles, h, k):
        # want to return something to denote if k is viable
        tot_hours = 0
        for pile in piles:
            # tot_hours += math.ceil(float(pile) / k)
            tot_hours += (pile + k - 1) // k # runs faster 
        
        return tot_hours <= h