class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        # try to assign values to the letters and directly calculate for queries? or more num manipulation to get it directly? 
        # also if letter not in equations return -1, then the same letter divided by itself is always 1
        # should be a graph prob -> defaultdict to store relation to other letters? 

        from collections import defaultdict, deque

        # 1. build the graph
        graph = defaultdict(dict) 
        # *
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val 

        # 2. bfs to find the product from source to target
        def bfs(start, end):
            if start not in graph or end not in graph: # takes care of undefined var
                return -1.0
            if start == end: # the same letter divided by self
                return 1.0
            
            # *
            queue = deque([(start, 1.0)])
            visited = {start}

            while queue:
                curr, cur_prod = queue.popleft()

                if curr == end: # reached answer
                    return cur_prod

                # *
                for neighbor, weight in graph[curr].items():
                    if neighbor not in visited: 
                        visited.add(neighbor)
                        # * find path C to D and multiply prod along the way
                        queue.append((neighbor, cur_prod * weight))
                        
            return -1.0

        # the above is for a single query, need to process all of them
        results = []
        for query in queries:
            c, d = query
            results.append(bfs(c, d))
            
        return results