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

    def get_first(self) -> Node[T]:
        return self._front
    
    def get_last(self) -> Node[T]:
        return self._back 
    
    def before(self, p: Node[T]) -> Node[T]:
        """
        Returns node immediately before node p
        """
        if p is None or self._front is p:
            return None
        return p.get_prev()
    
    def after(self, p: Node[T]) -> Node[T]:
        """
        Returns node immediately after node p
        """
        if p is None:
            return None 
        return p.get_next()
    
    def insert_before(self, p: Node[T], e: Node[T]) -> None:
        """
        Inserts the node e immediately before the node p
        """
        if e is None:
            return None 
        if p is None: 
            if self.is_empty():
                self._front = e
                self._back = e
                self._size += 1
                return 
            else: 
                return None
        
        if self.get_first() is p:
            p.set_prev(e)
            e.set_next(p)
            self._front = e
            self._size += 1
        else: 
            temp = self.get_first()
            while temp is not None and temp.get_next() != p:
                temp = temp.get_next()
            if temp is None:
                return None 
            temp.set_next(e)
            p.set_prev(e)
            e.set_next(p)
            e.set_prev(temp)
            self._size += 1

    def insert_after(self, p: Node[T], e: Node[T]) -> None:
        """
        Inserts the node e immediately after the node p
        """
        if e is None:
            return None 
        
        if p is None:
            if self.is_empty():
                self._front = e 
                self._back = e
                self._size += 1
                return 
            else:
                return None 
            
        if self.get_last() is p:
            p.set_next(e)
            e.set_prev(p)
            self._back = e 
            self._size += 1
        else:
            temp = self.get_first()
            while temp is not None and temp.get_prev() != p:
                temp = temp.get_next() 
            if temp is None: 
                return 
            temp.set_prev(e)
            p.set_next(e)
            e.set_next(temp)
            e.set_prev(p)
            self._size += 1

    def remove(self, p: Node[T]) -> Node[T]:
        if p is None or self.is_empty():
            return None

        if self.get_first() is p:
            self._front = p.get_next()
            if self.size() == 1:
                self._back = p.get_next()
            self._size -= 1
            return p
        
        temp = self.get_first()
        while temp is not None and temp.get_next() != p:
            temp = temp.get_next()
        if temp is None:
            return None 
        node_next = p.get_next()
        temp.set_next(node_next)
        if node_next is None: 
            self._back = temp
        else:
            node_next.set_prev(temp)
        self._size -= 1
        return p
    
    def size(self) -> int:
        return self._size 
    
    def is_empty(self) -> bool: 
        return self._size == 0
