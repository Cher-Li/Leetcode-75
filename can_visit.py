class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        stack = [0]
        
        while stack:
            room = stack.pop()
            if room not in visited:
                visited.add(room)
                # all keys found in the current room to the stack
                for key in rooms[room]:
                    if key not in visited:
                        stack.append(key)
                        
        # if the number of visited rooms = tot number of rooms, true
        return len(visited) == len(rooms)