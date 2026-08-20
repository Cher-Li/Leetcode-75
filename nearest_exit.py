# *
from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        
        # feels like a backtracking problem, just finding the shortest path to an exit instead of just the first one? 
        # well ok graph prob so bfs, extend out and each "round" of spreading increments the num of steps

        # steps = 0

        # * just wrap up the whole thing instead of separate steps
        queue = deque([(entrance[0], entrance[1], 0)]) # (row, col, steps)
        
        # need to mark entrance as visited as well since entrance != exit
        maze[entrance[0]][entrance[1]] = '+'

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        # would also need to double check valid in maze as well as valid in terms of it's not + (wall) 
        m, n = len(maze), len(maze[0])

        # def bfs(maze, location):
        #     for d in directions:
        #         row, col = entrance
        #         new_entrance = [row + d[0], col + d[1]] # need to check if not wall

        #         steps += 1
        #         if new_entrance[0] > m or new_entrance[1] > n: # needs to be empty cell at the border, so also check < 0? 
        #             return steps
        
        # bfs(maze, entrance)

        while queue:
            r, c, steps = queue.popleft()

            for d in directions: 
                new_row, new_col = r + d[0], c + d[1]

                # adds the 0 thing
                if 0 <= new_row < m and 0 <= new_col < n and maze[new_row][new_col] == '.': 
                    # checking if exit
                    if new_row == 0 or new_row == m - 1 or new_col == 0 or new_col == n - 1:
                        return steps + 1 # * need the + 1
                    
                    # else mark as visited and keep appending
                    maze[new_row][new_col] = '+'

                    queue.append((new_row, new_col, steps + 1))
                    
        return -1 # if reached end of queue and no return