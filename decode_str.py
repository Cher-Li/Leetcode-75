class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # stack vibes, when you reach a number you would have to repeat the [] that follows that many times
        # start from inside out, so when reach an ending bracket duplicate the last [] or something like that
        # not sure if use recursion in this case and just keep decode smaller and smaller strings? 

        stack = []
        # * instead of sub lists use this var to track
        cur_string = ""
        num = 0 

        for c in s:
            if c.isdigit(): # * func name
                # num = c
                num = num * 10 + int(c) # * int can be greater than 9
            elif c == "[":
                # somehow start the stack, how does this work w/ nested stacks tho? <- change to str instead
                # cur_stack = []
                # * basically just reset and start new instance
                stack.append((cur_string, num)) # * like, literally save the context onto stack and use cur_str to do the work
                cur_string = ""
                num = 0
            elif c == "]": 
                # need to take everything from the previous [ onwards and repeat it by the num before? 
                # stack.append(num * cur_stack)

                # *
                prev_str, prev_num = stack.pop()
                cur_string = prev_str + (prev_num * cur_string)
            else: 
                # cur_stack.append() 
                cur_string += c
        
        return cur_string