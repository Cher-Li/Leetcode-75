from collections import defaultdict

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        # so I was thinking, you need to go over the entire arr to count the number of occurrences
        # maybe like a dictionary of value : freq? 
        # and we have to ensure the different frequencies are unique, maybe go over all frequencies and add them to a set, then return len(set) == len(dict) since if there are duplicates the set would be less? 

        count = defaultdict(int)
        for num in arr:
            count[num] += 1
        
        # no_duplicates = set(int)
        no_duplicates = set()

        # * also not just count
        # for num, freq in count.items():
        # * or the following 
        for freq in count.values(): 
            # * append vs add
            no_duplicates.add(freq)
        
        return len(no_duplicates) == len(count)