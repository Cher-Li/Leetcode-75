from bisect import bisect_left

# version from online, wrong answer for spells = [5,1,3] and potions = [1, 2, 3, 4, 5]
class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        num_potions = len(potions)
        result = []

        for spell_strength in spells:
            # min_potion_strength = success / spell_strength 
            # nvm still need the below
            min_potion_strength = (success + spell_strength - 1) // spell_strength

            # directly find leftmost position where potion >= limit
            insert_position = bisect_left(potions, min_potion_strength)

            result.append(num_potions - insert_position)

        return result

# class Solution(object):
#     def successfulPairs(self, spells, potions, success):
#         """
#         :type spells: List[int]
#         :type potions: List[int]
#         :type success: int
#         :rtype: List[int]
#         """
        
#         answer = []
#         # successful if product of pairs is at least success
#         # naive solution is just to loop through len of spells, multiply spells with each potion in potions, keep appending to result
#         # but I guess given the spell, potion would need to be at least success / spells? So possibly sort potions and pick out ones greater than that? 

#         # so sort the potions arr first, then find the limit w/ binary search
#         # * not finding the limit but finding the first that gets past the limit
#         potions.sort()

#         for spell in spells:
#             # limit = success / spell 
#             # * ceiling division, min required potion limit
#             limit = (success + spell - 1) // spell
#             left = 0
#             right = len(potions) # * half open interval, edge case of if no potion is strong enough, then left moves to right and equals len(potions) so answer appends 0

#             # * lower bound binary search
#             while left < right: 
#                 # find limit within potions
#                 mid = (right + left) // 2

#                 # * this only works if the limit exists
#                 # if potions[mid] == limit:
#                 #     # mid is the index of limit
#                 #     answer.append(len(potions) - left) # * - left vs mid
#                 #     break
                
#                 if potions[mid] < limit:
#                     # limit is to the right
#                     left = mid + 1
#                 # elif potions[mid] > limit:
#                 else: # valid, could == limit, just trying to find the closest to the limit
#                     # right = mid - 1
#                     right = mid # b/c potions[mid] could be the answer
                
#             answer.append(len(potions) - left) # * automatically know that got to the right index
        
#         return answer