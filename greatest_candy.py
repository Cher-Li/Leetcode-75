class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        # loop through candies for the current max <- or maybe built in func
        # if candies[i] + extra is >= that max, return true

        cur_max = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= cur_max:
                result.append(True)
            else:
                result.append(False)
        
        return result