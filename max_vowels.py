class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # direct approach is just, keep window of length k, count number of vowels, if when slide out remove a vowel decrement cur count, otherwise if incoming vowel increment
        vowels = 'aeiou' 
        cur_num = 0
        for i in range(k):
            if s[i] in vowels:
                cur_num += 1
        max_num = cur_num

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                cur_num -= 1
            
            if s[i] in vowels:
                cur_num += 1
            
            max_num = max(max_num, cur_num)

        return max_num
        # O(n) time and O(1) space