class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        # * sort based on ending x-coords, similar to prev interval prob
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        current_arrow_pos = points[0][1]
        
        for i in range(1, len(points)):
            # if cur balloon starts after last arrow position, new arrow
            if points[i][0] > current_arrow_pos:
                arrows += 1
                current_arrow_pos = points[i][1]
                
        return arrows