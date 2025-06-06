from typing import Generic, TypeVar 

T = TypeVar('T')

class Node(Generic[T]):

    def __init__(self, value: T, next: 'Node[T]' = None) -> None: 
        self._value = value 
        self._next = next 

    
    def get_value(self) -> T: 
        return self._value 
    
    def set_value(self, value: T) -> None: 
        self._value = value

    def get_next(self) -> 'Node[T]':
        return self._next 

    def set_next(self, next: 'Node[T]') -> None:
        self._next = next

    