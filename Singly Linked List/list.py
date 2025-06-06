from node import Node 
from typing import Generic, TypeVar 

T = TypeVar('T')

class Singly_list(Generic[T]):

    _size: int
    _front: Node[T]
    _back: Node[T]

    
    def __init__(self, first_node: Node[T]) -> None: 
        self._size = 1
        self._front = first_node
        self._back = first_node 

    def first(self) -> Node[T]:
        return self._front
    
    def last(self) -> Node[T]:
        return self._back 
    
    def after(self, p: Node[T]) -> Node[T]:
        if p is None:
            return None 
        
        return p.get_next()
    
    def insert_after(self, p: Node[T], e: Node[T]) -> None: 
        """
        Inserts node e immediately after node p 
        """

        if p is None:
            if self.size() == 0:
                self._size = 1
                self._front = e 
                self._back = e
            else:
                e.set_next(self._front)
                self._front = e 
                self._size += 1 

        elif p.get_next() is None: 
            p.set_next(e)
            self._back = e 
            self._size += 1 

        else: 
            temp = p.get_next() 
            p.set_next(e)
            e.set_next(temp)
            self._size += 1


    def remove(self, p: Node[T]) -> Node[T]:
        if p is None: 
            return None 
        
        if p == self.first():
            self._front = p.get_next()
            if self._front is None: 
                self._back = None 
            self._size -= 1 
            return p 
        else: 
            temp = self.first() 
            while temp is not None and temp.get_next() != p: 
                temp = temp.get_next()
            if temp is None: 
                return None
            
            temp.set_next(p.get_next())
            if temp.get_next() is None:
                self._back = temp
            self._size -= 1
            return p
        
    def size(self) -> int:
        return self._size 
    
    def is_empty(self) -> bool:
        return self._size == 0
            

                
    