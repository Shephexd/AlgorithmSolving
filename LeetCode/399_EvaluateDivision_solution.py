class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.get_graph(equations, values, queries)
        res = []
        print(graph)
        for query in queries:
            res.append(self.search(graph, query, []))
        return res
    
    def search(self, graph, query, visited, acc=1):
        start, end = query
        if start not in graph:
            return -1
        
        if start == end:
            return 1
        
        if end in graph[start]:
            return acc * graph[start][end]
        
        if query in visited:
            return -1
        
        for next_key in graph[start]:
            next_query = [next_key, end]
            visited.append(query)
            res = self.search(graph, next_query, visited, acc * graph[start][next_key])
            visited.pop()
            if res != -1:
                return res
        return -1
        
    def get_graph(self, equations, values, query):
        graph = dict()
        
        for equation, value in zip(equations, values):
            left_equation_val, right_equation_val = equation
            
            if left_equation_val not in graph:
                graph[left_equation_val] = dict()
            if right_equation_val not in graph:
                graph[right_equation_val] = dict()
            
            graph[left_equation_val][right_equation_val] = value
            graph[right_equation_val][left_equation_val] = 1/value
        return graph
