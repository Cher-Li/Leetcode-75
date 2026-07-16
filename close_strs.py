from collections import defaultdict

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        # can swap existing characters, can change all of one letter to another
        # 1. they need to have the same unique letters 2. I guess they need the same frequency of characters not necessarily for the same characters? 

        # maybe a defaultdict to count up "freq" aka number of a specific chara
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        set1 = set()
        set2 = set()

        for c in word1:
            dict1[c] += 1
            set1.add(c)
        for c in word2:
            dict2[c] += 1
            set2.add(c)

        # then check same freq and that the two sets are the same? 
        if set1 != set2: # yea you can just directly compare like this
            return False 
        
        # *
        return sorted(dict1.values()) == sorted(dict2.values())

# from collections import Counter

# class Solution(object):
#     def closeStrings(self, word1, word2):
#         # or simpler, might have slower runtime tho? 
#         c1 = Counter(word1)
#         c2 = Counter(word2)

#         return set(c1.keys()) == set(c2.keys()) and sorted(c1.values()) == sorted(c2.values()) 
    
#     # or even: 
#     # return c1.keys() == c2.keys() and sorted(c1.values()) == sorted(c2.values())