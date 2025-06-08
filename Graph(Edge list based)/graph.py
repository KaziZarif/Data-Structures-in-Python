from typing import TypeVar, Generic, List
from vertex import Vertex
from edge import Edge

T = TypeVar('T')

class Graph(Generic[T]):
    _vertices: List[Vertex[T]]
    _edges: List[Edge[T]]


    def __init__(self) -> None:
        self._vertices = []
        self._edges = []

    def num_vertices(self) -> int:
        return len(self._vertices) 
    
    def list_vertices(self) -> List[Vertex[T]]:
        return self._vertices
    
    def num_edges(self) -> int:
        return len(self._edges) 
    
    def list_edges(self) -> List[Edge[T]]:
        return self._edges 
    
    def get_edge(self, u: Vertex[T], v: Vertex[T]) -> Edge[T]:
        if u is None or v is None:
            return None
        
        for edge in self._edges:
            if (edge.get_vertex_u() == u and edge.get_vertex_v() == v) or (edge.get_vertex_u() == v and edge.get_vertex_v() == u):
                return edge 

        return None 
    
    def end_vertices(self, e: Edge[T]) -> List[Vertex[T]]:
        if e is None or e not in self._edges:
            return None 
        
        return [e.get_vertex_u(), e.get_vertex_v()]
    
    def opposite(self, v: Vertex[T], e: Edge[T]) -> Vertex[T]:
        if v is None or e is None:
            return None 
        
        if e in self._edges:
            if (e.get_vertex_u() == v):
                return e.get_vertex_v()
            elif (e.get_vertex_v() == v):
                return e.get_vertex_u()
            
        return None 
    
    def degree(self, v: Vertex[T]) -> int:
        if v is None:
            return None 
        
        degree = 0
        for edge in self._edges:
            if (edge.get_vertex_u() == v) or (edge.get_vertex_v() == v):
                degree += 1

        return degree 
    
    def incident_edges(self, v: Vertex[T]) -> List[Edge[T]]:
        if v is None:
            return None 

        edge_list = []
        for e in self._edges: 
            if (e.get_vertex_u() == v) or (e.get_vertex_v() == v):
                edge_list.append(e)
        
        return edge_list
    
    def insert_vertex(self, x: T) -> Vertex[T]:
        if x is None:
            return None 
        
        v = Vertex(x)
        self._vertices.append(v)
        return v
    
    def insert_edge(self, u: Vertex[T], v: Vertex[T], x: T) -> Edge[T]:
        if u is None or v is None:
            return None 
        
        if u not in self._vertices or v not in self._vertices:
            return None
        
        for edge in self._edges:
            if (edge.get_vertex_u() == u and edge.get_vertex_v() == v) or (edge.get_vertex_u() == v and edge.get_vertex_v() == u):
                return None 

        e = Edge(x, u, v)
        self._edges.append(e)
        return e

    def remove_vertex(self, v: Vertex[T]) -> None:
        if v is None:
            return None 
        

        for edge in self._edges: 
            if (edge.get_vertex_v() == v) or (edge.get_vertex_u() == v):
                self._edges.remove(edge)

        if v in self._vertices:
            self._vertices.remove(v) 


    def remove_edge(self, e: Edge[T]) -> None: 
        if e is None:
            return None 

        if e in self._edges: 
            self._edges.remove(e) 
         
        
        