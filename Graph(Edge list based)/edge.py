from typing import TypeVar, Generic

T = TypeVar('T')

class Edge(Generic[T]):
    _element: T
    _u: 'Vertex[T]'
    _v: 'Vertex[T]'

    def __init__(self, element: T, u: 'Vertex[T]' = None, v: 'Vertex[T]' = None) -> None:
        self._element = element 
        self._u = u 
        self._v = v

    def get_element(self) -> T:
        return self._element 
    
    def get_vertex_u(self) -> 'Vertex[T]':
        return self._u 
    
    def get_vertex_v(self) -> 'Vertex[T]':
        return self._v 
    
    