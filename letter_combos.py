class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits:
            return []

        answer = [""]
        # backtracking vibes, digits matching multiple letters tho

        d = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"] # * index i corresponds with digit i + 2

        for digit in digits:
            letters = d[int(digit) - 2]
          
            # * append each letter to each existing combination
            answer = [existing + letter 
                     for existing in answer 
                     for letter in letters]
      
        return answer