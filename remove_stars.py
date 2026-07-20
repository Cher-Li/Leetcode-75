class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # basically wherever there are *, that number of characters is omitted from its left
        # vaguely reminds me of a stack prob
        # like if the newest character is a *, pop from the stack, then you're left with the end 

        stack = []
        for c in s:
            if c != "*":
                stack.append(c)
            else:
                stack.pop()
        
        return "".join(stack) # * just remember to do this