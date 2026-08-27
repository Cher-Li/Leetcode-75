import heapq

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        # naive solution is just brute force, loop through and get length k and calc score = sum of nums1 values and min of nums2 ones <- also doesn't work because you can pick not-continuous indices
        # like, want the max of the min of the latter? 

        # max product if min is nums2[i] then involve k? 

        # * 
        pairs = sorted(zip(nums2, nums1), reverse = True) # pair the two arrays, sort in descending order so largest nums2 value at the start
        min_heap = []
        cur_sum = 0
        max_score = 0

        for n2, n1 in pairs: 
            # calc for sum of nums1
            heapq.heappush(min_heap, n1)
            cur_sum += n1 

            # * if heap size too big, remove the smallest on the heap
            if len(min_heap) > k: 
                removed = heapq.heappop(min_heap)
                cur_sum -= removed
            
            # if reached the size k, calc the final product
            if len(min_heap) == k:
                max_score = max(max_score, cur_sum * n2)
        
        return max_score