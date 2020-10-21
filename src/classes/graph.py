"""
Graph class that will build all the connections between the Addresses
Thank you, Zybooks!
"""
from classes.vertex import Vertex

class Graph:
    def __init__(self):
        self.vertex_set = {}
        self.edge_weights = {}
        self.address_map = {} # Haxxorz at the expense of using more memory..
        
    def add_vertex(self, new_vertex: Vertex) -> None:
        self.vertex_set[new_vertex] = []
        self.address_map[new_vertex.name] = new_vertex
        
    def __add_directed_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight: float) -> None:
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.vertex_set[from_vertex].append(to_vertex)
        
    def add_undirected_edge(self, vertex_a: Vertex, vertex_b: Vertex, weight: float) -> None:
        self.__add_directed_edge(vertex_a, vertex_b, weight)
        self.__add_directed_edge(vertex_b, vertex_a, weight)

    def get_address_distance(self, start: str, end: str) -> float:
        vertex_1 = self.address_map[start]
        vertex_2 = self.address_map[end]
        return self.edge_weights[(vertex_1, vertex_2)]
