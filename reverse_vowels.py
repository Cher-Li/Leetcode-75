class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # something like, keeping track of indices of vowels
        # swap the first and last vowels and then both pointers increment towards the center? 

        # * because strings are immutable
        s = list(s)

        ptr1, ptr2 = 0, len(s) - 1
        while ptr1 < ptr2: # * might cross w/o being equal? 
            # * check the value of ptr, also capitals
            if s[ptr1] not in "aeiouAEIOU": 
                ptr1 = ptr1 + 1
            
            if s[ptr2] not in "aeiouAEIOU": 
                ptr2 = ptr2 - 1
            
            if s[ptr1] in "aeiouAEIOU" and s[ptr2] in "aeiouAEIOU":
                s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
                ptr1 += 1
                ptr2 -= 1 # * 
        
        return "".join(s)