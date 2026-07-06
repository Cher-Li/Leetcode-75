from collections import defaultdict

# class Solution(object):
#     def maxOperations(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
        
#         # find the max num of pairs that sum to k that don't overlap
#         # I was thinking something to count up the frequencies of each num to match is against k - nums later on
#         # loop through to get freq then loop through again the find matches? 
#         # and take the min frequency of each pair because that's the num of operations 

#         # frequency method: 
#         # min of each pair, also need to make sure (2, 3) and (3, 2) aren't counted separately -> deduct after first pair, or keep a visited set
#         # what if [3, 3, 3, 3] <- freq is equal but need pairs of 2

#         # build map
#         # frequency = {} # defaultdict so no error when no key found? 
#         frequency = defaultdict(int)

#         for val in nums:
#             frequency[val] += 1

#         answer = 0
#         for num in frequency: 
#             complement = k - num

#             if complement not in frequency:
#                 continue

#             # match up pairs
#             if num == complement:
#                 answer += frequency[num] // 2 # if especially pair with each other
#                 frequency[num] = 0

#             else: 
#                 # count in answer then remove so no double counting
#                 pairs = min(frequency[num], frequency[complement])
#                 answer += pairs
#                 frequency[num] -= pairs
#                 frequency[complement] -= pairs
        
#         return answer

# with hash map, pair as you go
class Solution(object):
    def maxOperations(self, nums, k):
        counts = defaultdict(int)
        ans = 0

        for x in nums: 
            # if match, immediately decrement num
            if counts[k - x] > 0:
                ans += 1
                counts[k - x] -= 1
            else:
                # else just add to the "freq" 
                counts[x] += 1
        
        return ans