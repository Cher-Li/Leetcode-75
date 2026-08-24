import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # could keep a max heap, then kth largest in the heap? 
        # only keep the k largest element and just return the smallest of the final max heap? 

        heap = []

        for num in nums:
            # * append first
            heapq.heappush(heap, num) # also remember to pass in heap

            # check if heap length is > k
            if len(heap) > k: 
                # want to remove the smallest one
                heapq.heappop(heap)
        
        # * top of heap should be kth largest
        return heap[0]
        # O(n log K) time and O(K) space
        # quick select works best in practice b/c O(N) time and space, keep searching into the left vs right area otherwise return that pivot