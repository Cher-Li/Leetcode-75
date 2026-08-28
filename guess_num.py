# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # guessed_num = n / 2
        start = 1
        end = n

        while start <= end: 
            guessed_num = (end + start) // 2
            result = guess(guessed_num)
            if result == 0:
                return guessed_num
            
            if result < 1:
                # guess is higher than num so narrow towards lower end
                end = guessed_num - 1
            # guess lower gives result of 1 exactly
            elif result == 1:
                start = guessed_num + 1