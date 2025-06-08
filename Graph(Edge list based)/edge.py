from typing import TypeVar, Generic

T = TypeVar('T')

class Edge(Generic[T]):
    _element: T
    _u: 'Vertex[T]'
    _v: 'Vertex[T]'

    