class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # maybe given s, split by spaces
        # then the usual reversal of switching first and last words? 

        words = s.split()
        ptr1, ptr2 = 0, len(words) - 1
        while ptr1 < ptr2:
            words[ptr1], words[ptr2] = words[ptr2], words[ptr1]

            ptr1 = ptr1 + 1
            ptr2 = ptr2 - 1
        
        # * remember to space them out at the end
        return " ".join(words)

# or directly: 
# return " ".join(s.split()[::-1]) 