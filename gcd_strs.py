# from math import gcd

# * use this since no imports
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        # basically find the greatest overlap of letters that repeat
        # maybe start with shorter str and seeing if other str is concat of that with pointers? 
        # or like, check the ratio of letters, doesn't ensure order tho

        # str1 is x repeated for a times, str2 is x repeated for b times
        # can return "" if even vs odd because need to neatly divide both

        # x, other = 0
        # if len(str1) > len(str2):
        #     x = str2
        #     other = str1
        # else:
        #     x = str1
        #     other = str2

        # * if something evenly divides, then x + x + x... = x * i would get both answers, as well as both their concat
        # x * a + x * b = x * b + x * a
        if str1 + str2 != str2 + str1:
            return ""

        # or entirely find the gcd number and loop through the shorter str to check if viable <- has to divide both, so just take the first _ numbers
        d = gcd(len(str1), len(str2)) # length of largest string
        x = str1[:d] # should be the largest str that divides both
        # limit = max(len(str1) // d, len(str2) // d) 
        # construct_A = construct_B = False
        # for i in range(1, limit + 1):
        #     # need to check that x repeated constructs both strings
        #     if x * i == str1:
        #         construct_A = True
        #     if x * i == str2:
        #         construct_B = True
            
        #     if construct_A and construct_B:
        #         return x
        
        # return ""
        # or directly divide to see if evenly repeats, only one "i" possible to make up each str

        return x