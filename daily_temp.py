class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        # brute force is to calc each one by one start to finish
        # maybe something like, start from last temp, if i-1 is colder then it's a 1? Keep track of warmest? 
        # it's a monotonic stack prob tho, O(N) time
        # * keep track of indices of days that haven't found a warmer day yet

        n = len(temperatures)
        answer = [0] * n
        stack = [] # *

        for i in range(n):
            # if stack empty, no warmer days ahead so always 0
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # the moment find the right answer for the ones waiting
                prev_index = stack.pop() 
                answer[prev_index] = i - prev_index # difference between the two indices
            
            stack.append(i)
        
        return answer 