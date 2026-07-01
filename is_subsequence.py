class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # naive approach is just, loop through all letters and compare, N^len of s or something
        # sliding window to check each letter of s in t? 
        # and if encounter new letter check against s
        # possibly recursion by passing in the index and find subsequence in a substring? 

        # ptr = 0
        # for char in s:
        #     # * 
        #     found = False

        #     for i in range(ptr, len(t)):
        #         if t[i] == char:
        #             ptr = i + 1 # * + 1
        #             found = True
        #             break # should go to the next char
            
        #     if not found:
        #         return False
        #     # return False # got to end of len(t) and didn't find char
        #     # * doesn't work since only really checks the first char


        # return True
        

        # * more efficient to use two pointers
        i = 0 # for s
        j = 0 # for j

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1 # * always increment this
        
        return i == len(s) # so also takes care of if j went past len(t) aka false
