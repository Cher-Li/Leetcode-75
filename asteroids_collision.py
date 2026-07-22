class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        stack = []
        for asteroid in asteroids:
            # if asteroid > 0: 
            #     stack.append(asteroid)
            # else:
            #     # negative so collide w/ the leftmost asteroid on stack
            #     # oh and based on ex 3, it keeps popping until the on on the stack is greater in magnitude instead of just chipping away at the asteroid
            #     # * also, negative asteroid only collide with positive asteroids
            #     while stack: # like in case this negative asteroid goes all the way to the start
            #         prev = stack.pop()
            #         mag = abs(asteroid)
            #         if prev > mag:
            #             stack.append(prev)
            #             break
            #         elif prev == mag:
            #             break
            #         else: 

            #             # still need to append prev to stack if gets all the way to the end? 
            #             if not stack:
            #                 stack.append(asteroid)
            #                 break
            #             else:
            #                 continue
                    
            #         # 1. prev is bigger than asteroid -> put prev back on stack, break
            #         # 2. prev is equal to asteroid -> just break b/c prev also gets destroyed
            #         # 3. prev is less than asteroid -> continue

            while stack and asteroid < 0 and stack[-1] > 0: # * only collide if current asteroid moving left and top of stack is moving right
                diff = asteroid + stack[-1] # can just directly compare like this
                if diff < 0:
                    # more negative, need to keep going
                    stack.pop()
                elif diff > 0: 
                    # more positive, current asteroid destroyed
                    asteroid = 0
                    break
                else:
                    # equal so both destroyed
                    stack.pop()
                    asteroid = 0
                    break # break from this process but continue going through asteroids
            
            # * if asteroid survived, hence why set it to 0 above
            if asteroid != 0:
                stack.append(asteroid)
        
        return stack # O(N) complexity, every asteroid pushed / popped at most once