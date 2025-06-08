from node import Node 
from typing import  List

class PriorityQueue():
    _root: Node
    _last: Node
    _size: int 


    def __init__(self) -> None:
        self._root = None
        self._last = None 
        self._size = 0

    def size(self) -> int:
        return self._size 
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def min(self) -> Node: 
        if self.size() == 0:
            return None 
        return self._root 
    
    def insert(self, key: int, value: str) -> None:
        """
        Create and insert Node with key and value
        """

        if key is None or value is None:
            return None 

        new_node = Node(key, value)

        if self._root is None:
            self._root = new_node 
            self._last = new_node 
            self._size += 1
            return 
        
        # If all levels in the heap is filled
        if ((self.size() + 1) & self.size()) == 0:
            current = self._root
            while current.get_left_child() is not None:
                current = current.get_left_child()
            current.add_left_child(new_node)
            self._last = new_node 
            self._size += 1
            new_node.up_heap()
            return 

        # If the last node is a left child
        if self._last.get_parent().get_left_child() == self._last:
            self._last.get_parent().add_right_child(new_node)
            self._last = new_node
            self._size += 1
            new_node.up_heap()
            return 
        # Else if the last node is a right child
        else:
            current = self._last 
            while current.get_parent() and current == current.get_parent().get_right_child():
                current = current.get_parent()
            
            if current.get_parent():
                current = current.get_parent().get_right_child()
            
            while current.get_left_child():
                current = current.get_left_child()
            current.add_left_child(new_node)
            self._last = new_node 
            self._size += 1
            new_node.up_heap()
            return 
        
    def remove_min(self) -> Node:
        "Remove the node with the smallest key in the queue"

        if self.size() == 0:
            return None 
        if self.size() == 1:
            min_node = Node(self._root.get_key(), self._root.get_value())
            self._root = None 
            self._last = None 
            self._size -= 1
            return min_node 
        
        min_node = Node(self._root.get_key(), self._root.get_value())
        self._root.set_key(self._last.get_key())
        self._root.set_value(self._last.get_value())

        parent = self._last.get_parent()
        if parent.get_left_child() == self._last:
            parent.add_left_child(None)
        else:
            parent.add_right_child(None)
        self._size -= 1

        current = self._root 
        path = bin(self.size())[3:]
        for direction in path:
            if direction == '0':
                current = current.get_left_child()
            else:
                current = current.get_right_child()

        self._last = current 
        self._root.down_heap()
        return min_node 
