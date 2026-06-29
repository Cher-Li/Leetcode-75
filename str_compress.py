class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        # feels like a stack prob
        # stack.push the character, if consecutive repeating, just go until it no longer repeats
        # then append the number of repeats to s? 
        # should be stored in input chars tho so just remove repeating characters 
        # return len(chars) at the end
        # well, only keep a single character as reference since constant extra space? 
        # also need to focus on how 12 would be written as ["1", "2"] so push groups of tens? 

        # 2 pointers? One to keep track of current reference char (where to append?), the other counting number of repeats? 
        # read vs write pointers? 
        read, write = 1, 0 # read always ahead of write, init before the below
        # * init write as 0 b/c later chars[write] = cur_char so written again
        cur_char = chars[0] 
        counter = 1

        while read < len(chars):
            # if cur char matches the prev
            if chars[read] == cur_char:
                # write = write + 1 # nope literally only increment when needed
                counter = counter + 1

            # if new char
            else: 
                # chars[write] = counter 
                # * for tens place
                # also don't need to write if 1
                chars[write] = cur_char
                write += 1

                if counter > 1:
                    for digit in str(counter):
                        chars[write] = digit
                        write += 1
                
                # starting new group
                # also doesn't actually take care of repeating char tho? 
                # *
                cur_char = chars[read]

                counter = 1
            
            # *
            read += 1
        
        # * final group
        chars[write] = cur_char
        write += 1

        if counter > 1:
            for digit in str(counter):
                chars[write] = digit
                write += 1

        # also after finish reading, make sure write is also at the end of the char? 
        # return len(chars) 
        # * just compress and take the first part of what's written
        # don't need to worry abt shrinking the chars arr
        return write