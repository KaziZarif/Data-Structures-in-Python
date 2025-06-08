class Node():
    _key: int
    _value: str
    _parent: 'Node'
    _left_child: 'Node'
    _right_child: 'Node'

    def __init__(self, key: int, value: str) -> None:
        self._key = key
        self._value = value 
        self._parent = None 
        self._left_child = None 
        self._right_child = None 

    
    def get_key(self) -> int: 
        return self._key 
    
    def set_key(self, key: int) -> None: 
        self._key = key 

    def get_value(self) -> str:
        return self._value 
    
    def set_value(self, value: str) -> None: 
        self._value = value 

    def add_left_child(self, child: 'Node') -> None:
        if child == None 
            self._left_child = None 
            return 
        self._left_child = child
        child._parent = self 

    def add_right_child(self, child: 'Node') -> None:
        if child == None:
            self._right_child = None
            return
        self._right_child = child
        child._parent = self

    def get_left_child(self) -> 'Node':
        return self._left_child

    def get_right_child(self) -> 'Node':
        return self._right_child
    
    def is_root(self) -> bool:
        return self._parent == None 
    
    def up_heap(self) -> None:
        current = self

        while current.get_parent() and current.get_key() < current.get_parent().get_key():
            temp_key = current.get_key()
            temp_value = current.get_value()
            current.set_key(current.get_parent().get_key())
            current.set_value(current.get_parent().get_value())
            current.get_parent().set_key(temp_key)
            current.get_parent().set_value(temp_value)
            current = current.get_parent()

    def down_heap(self) -> None:
        current = self    
        while True:
            smallest = current

            if current.get_left_child() and current.get_left_child().get_key() < smallest.get_key():
                smallest = current.get_left_child()
            
            if current.get_right_child() and current.get_right_child().get_key() < smallest.get_key(): 
                smallest = current.get_right_child()

            if smallest == current:
                break
            
            temp_key = current.get_key()
            temp_value = current.get_value()
            current.set_key(smallest.get_key())
            current.set_value(smallest.get_value())
            smallest.set_key(temp_key)
            smallest.set_value(temp_value)
            current = smallest