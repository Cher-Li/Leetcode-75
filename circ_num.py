class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # maybe a set, keep track of all visited
        # loop through the different nodes, keep adding to the stack of what it's connected to and assign the same province? And just keep incrementng province? 

        n = len(isConnected)
        visited = [False] * n # * bool arr
        provinces = 0 # keep track of num
        
        def dfs(city): # just keep finding all of the connected cities from the input city
            visited[city] = True
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        
        for i in range(n): 
            if not visited[i]: 
                dfs(i)
                provinces += 1
                
        return provinces