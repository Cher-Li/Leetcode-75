class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        # convert to arr? 

        result = []
        
        # * = 0, 0
        ptr1, ptr2 = 0, 0
        # * and not or, both needs to be < for shared alternating
        while ptr1 < len(word1) and ptr2 < len(word2):
            # increment while alternating
            result.append(word1[ptr1])
            result.append(word2[ptr2])
            # * remember to increment
            ptr1 = ptr1 + 1
            ptr2 = ptr2 + 1
        
        # then append the final letters onto end of merged str
        # * not whether ptr1 < ptr2 but if ptr1 < len(word1) and so on

        while ptr2 < len(word2):
            result.append(word2[ptr2])
            ptr2 = ptr2 + 1

        while ptr1 < len(word1):
            result.append(word1[ptr1]) 
            ptr1 = ptr1 + 1
        
        # * also returns str
        return "".join(result)