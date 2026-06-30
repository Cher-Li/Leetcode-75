class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # another read / write prob maybe? 
        # could either focus on moving all 0s to end
        # or bring any non zero elements to the beginning in order

        # might go with the latter, keep a writer ptr and just overwrite stuff since read is always ahead, and fill the rest with zeroes

        read, write = 0, 0
        while read < len(nums):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
            
            read += 1
        
        # and then deal w/ rest of zeroes
        while write < len(nums):
            nums[write] = 0
            write += 1