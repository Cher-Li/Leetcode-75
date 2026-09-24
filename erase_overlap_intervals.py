class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x : x[1]) # sort by end times
        ans = 0
        prev_end = intervals[0][1]
        
        # would a greedy method work where the moment something overlaps you remove it? 
        for i in range(1, len(intervals)):
            # and just keep track of the latest interval? 
            start, end = intervals[i]

            # overlap when starts before the prev ends
            if start < prev_end:
                ans += 1
            else: # else just keep updating the end
                prev_end = end
        # O(N log N) time
        
        return ans