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

        