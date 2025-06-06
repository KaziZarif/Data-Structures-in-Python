class Item():
    _key: int
    _value: str

    def __init__(self, key: int, value: str) -> None: 
        self._key = key 
        self._value = value

    def get_key(self) -> int: 
        return self._key
    
    def get_value(self) -> str:
        return self._value