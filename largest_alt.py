class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        # most straightforward is just, actually create altitude, so like alt[0] = 0, then alt[i] = alt[i-1] + gain[i-1]? 
        # or not storing all alt just the current alt, keep incrementing and keeping track of the largest alt

        max_alt = 0 # always start w/ 0 so that would be the max or above
        alt = 0
        for num in gain:
            alt = num + alt
            max_alt = max(alt, max_alt)

        return max_alt # O(1) space