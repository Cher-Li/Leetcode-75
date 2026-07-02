class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # start with the ends and gradually move inwards? 
        # like if the inner is higher, possible that the height overcomes the decreased width
        # and area in general is what, (end - start) * min of values(end, start)? 

        start = 0
        end = len(height) - 1 # *
        area = 0 

        while start < end:
            local_area = (end - start) * min(height[end], height[start]) 
            area = max(area, local_area) 

            # then increment inwards? 
            # if height[start + 1] > height[start]:
            #     start += 1
            # if height[end - 1] > height[end]: 
            #     end -= 1

            # * just directly compare the two heights
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        
        return area
