from typing import TypeVar, Generic 

T = TypeVar('T')

class Vertex(Generic[T]):
    _element: T

    def __init__(self, element: T) -> None:
        self._element = element 

    def get_element(self) -> T
        return self._element