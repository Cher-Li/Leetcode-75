class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        
        # straightforward is to go through c, check a or b for that specific position? if c is 0 and a or b is 1, at least one flip? 
        # and if c is 1, either a or b should have a 1
        flips = 0

        # how to get the actual bits? We know a to c are all <= 10^9? 
        for bit_position in range(32):
            # * extracting the specific bit
            bit_a = (a >> bit_position) & 1
            bit_b = (b >> bit_position) & 1
            bit_c = (c >> bit_position) & 1 

            if bit_c == 0:
                # a and b both have to be zero
                if bit_a == 1:
                    flips += 1
                if bit_b == 1: 
                    flips += 1
                # * flips += bit_a + bit_b 
            
            else:
                # either bit a or b need to be 1
                if bit_a == 1 or bit_b == 1:
                    continue
                else:
                    flips += 1
                # * flips += int(bit_a == 0 and bit_b == 0) 
                # like if both 0, int is 1, otherwise false so 0
        
        return flips