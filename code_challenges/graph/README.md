# Graphs

* A graph is a non-linear collection or potentially collected nodes.

## Challenge

* Create a graph implementation with the following classes: [Graph, Vertex, Edge] and the following methods inside Graph class: [add_node, add_edge, get_nodes, get_neighbors, size].

## Approach & Efficiency

* The Graph class was created with the methods mentioned about. This class uses the Vertex class to instantiate new nodes and the Edge class to instantiate new edges.
* Note that all methods utilized have space and time efficiency of O(1).

## API

def add_node(self, val) -> *returns the node being created*
add_edge(self, start, end, weight=1) -> obj:
get_nodes(self) -> list:
get_neighbors(self, vertex) -> dict:
size(self) -> str:

## Code

[Code](/python/graphs/grephs.py)

## test

[test](/python/tests/test_graphs.py)
