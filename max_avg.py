# class Solution(object):
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#         """
        
#         # direct approach is just check all windows of size k and keeping running count of max avg 
#         # I mean since they're all length k just find the max overall sum of k consec elements? 

#         max_sum = 0
#         for i in range(k):
#             max_sum += nums[i]
#         # the above would be the first window
#         # then we want to remove the first elmt and add the next for each new window? 
#         cur_sum = max_sum
#         start = 0
#         for i in range(k, len(nums)):
#             cur_sum -= nums[start]
#             start += 1
#             cur_sum += nums[i]

#             max_sum = max(max_sum, cur_sum)

#         # return max_sum / k
#         # *
#         return float(max_sum) / k

class Solution(object):
    def findMaxAverage(self, nums, k):
        cur_sum = sum(nums[:k]) # instead of the for i in range k
        max_sum = cur_sum

        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i - k] # to avoid keeping track of start
            max_sum = max(max_sum, cur_sum)

        return float(max_sum) / k