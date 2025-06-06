from typing import List 
from item import Item 

class PriorityQueue(): 

    _sorted_list: List[Item]

    def __init__(self) -> None:
        self._sorted_list = []

    def size(self) -> int:
        return len(self._sorted_list)
    
    def is_empty(self) -> bool:
        return len(self._sorted_list) == 0
    
    def insert(self, key: int, value: str) -> None: 
        if key is None or value is None:
            return None 
        
        new_item = Item(key, value)
        low = 0
        high = self.size()
        while low < high: 
            mid = (low + high) // 2
            if new_item.get_key() > self._sorted_list[mid].get_key():
                low = mid + 1
            else:
                high = mid 
        self._sorted_list.insert(low, new_item) 

    def remove_min(self) -> Item: 
        if self.is_empty():
            return None 
        min_key = self._sorted_list[0]
        self._sorted_list.pop(0)
        return min_key
    
    def min(self) -> Item:
        if self.is_empty():
            return None 
        return self._sorted_list[0]