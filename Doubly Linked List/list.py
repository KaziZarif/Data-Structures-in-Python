from node import Node 
from typing import Generic, TypeVar

T = TypeVar('T')

class DoublyLinkedList(Generic[T]):
    _size: int 
    _front: Node[T]
    _back: Node[T] 

    def __init__(self, front: Node[T] = None) -> None: 
        self._size = 1 if front else 0
        self._front = front
        self._back = front

    def first(self) -> Node[T]:
        
