# class Solution(object):
#     def pivotIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        
#         # pivot index i, sum of [:i] = sum [i+1:], not counting i itself
#         # I mean I think the most straightforward solution is just, find the sum to the left of all indices vs right, then find the index where they're the same

#         prefix = [0] * len(nums)
#         postfix = [0] * len(nums)
#         for i in range(1, len(nums)):
#             prefix[i] = nums[i - 1] + prefix[i - 1] 
#         for j in range(len(nums) - 2, 0, -1):
#             # * oh yea len(nums) - 2 b/c last elmt is -1, but want the one before that b/c last one is automatically 0
#             postfix[j] = nums[j + 1] + postfix[j + 1]
#         # then if prefix == postfix return that leftmost pivot, otherwise -1, not sure if that's most efficient tho - O(N) for space rn
#         for i in range(len(nums)):
#             if prefix[i] == postfix[i]:
#                 return i

#         return -1

# * don't need to store every right sum b/c could calc it directly
class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums) # * could do this directly and just isolate the specific left vs right sums, I'm guessing it's more complicated w/ multiplication b/c of zeroes since it's irreversible? 
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            left += nums[i]

        return -1