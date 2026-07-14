class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        # answer would be a List[List[int]]? 
        # brute force would just be going through the shorter nums arr and checking if that num is in the other array, if find, skip, if not, add it to answer <- might also delete both so what's left is unique to the other array? Probably not the most efficient considering would deal with shifting elmts
        # also use a set to check for distinct ints? 
        # or the arrays themselves convert to set to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2) 

        # ans1 = ans2 = [] # * oh yea can't do this b/c they point to same place
        ans1 = []
        ans2 = []
        for num in set1:
            if num not in set2:
                ans1.append(num)
        
        for num in set2:
            if num not in set1:
                ans2.append(num)
        
        return [ans1, ans2]

# * or the below if allowed
# set1 = set(nums1)
# set2 = set(nums2)
# return [list(set1 - set2), list(set2 - set1)]