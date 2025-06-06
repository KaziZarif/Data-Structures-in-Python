from typing import Generic, TypeVar 

T = TypeVar('T')

class Node(Generic[T]):
    _value: T
    _next: 'Node[T]'
    _prev: 'Node[T]'

    def __init__(self, value: T, next: 'Node[T]' = None, prev: 'Node[T]' = None) -> None:
        self._value = value 
        self._next = next
        self._prev = prev

    def get_value(self) -> T:
        return self._value 
    
    def set_value(self, value: T) -> None:
        self._value = value

    def get_next(self) -> 'Node[T]':
        return self._next 
    
    def set_next(self, next: 'Node[T]') -> None:
        self._next = next

    def get_prev(self) -> 'Node[T]':
        return self._prev 
    
    def set_prev(self, prev: 'Node[T]') -> None:
        self._prev = prev
