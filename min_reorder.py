from collections import defaultdict

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
        # maybe work backwards, see what cities 0 is connected to, then it's reordering routes to make further paths lead to the new city? 
        # dfs from root, if a forward connection, need to reverse, and just count upwards? 

        # count = 0
        graph = defaultdict(list)
        for u, v in connections: 
            graph[u].append((v, 1)) # forward edge, need reverse if u -> v
            graph[v].append((u, 0)) # backward edge, correct in reaching node 0
        visited = set()

        # def dfs(node, connections):
        #     # checking all connections and increment count? 
        #     # like, given the city num and connections ig? 

        #     # ofc slow so, find another method
        #     for i in range(len(connections)):
        #         a, b = connections[i]
        #         if a < b:
        #             connections[i] = [b, a]
        #             count += 1
        # dfs(root, connections)

        count = [0] # mutable int
        def dfs(node): 
            # nonlocal count
            visited.add(node)

            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    count[0] += cost # basically just directly add 1 if forwrad edge
                    dfs(neighbor)
        
        dfs(0)
        return count[0] # O(N) 