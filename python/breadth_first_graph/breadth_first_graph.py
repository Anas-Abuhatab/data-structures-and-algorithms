from graphs.grephs import Graph

class Graph(Graph):
   def breadth_first(self, vertex):
        nodes = []
        breadth = [vertex]
        visited = set() 
        
        visited.add(vertex)
        
        while breadth:
            front = breadth.pop(0)
            nodes.append(front.value)
            
            for neighbor in self.get_neighbors(front):
                if neighbor.vertex not in visited:
                    visited.add(neighbor.vertex)
                    breadth.append(neighbor.vertex)

                    
        return nodes
