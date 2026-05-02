class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashmap = [None] * self.capacity

    def insert(self, key: int, value: int) -> None:
        idx = self._hash(key)

        while True:
            if self.hashmap[idx] == None:
                self.hashmap[idx] = Pair(key, value)                
                self.size += 1
                if self.size >= self.capacity / 2:
                    self.resize()   
                return  
            elif self.hashmap[idx].key == key:
                self.hashmap[idx].val = value
                return
            
            idx += 1
            idx = idx % self.capacity

    def get(self, key: int) -> int:
        idx = self._hash(key)

        while self.hashmap[idx] != None:
            if self.hashmap[idx].key == key:
                return self.hashmap[idx].val
            idx += 1
            idx = idx % self.capacity
        return -1

    def remove(self, key: int) -> bool:
        idx = self._hash(key)
        while self.hashmap[idx] != None:
            if self.hashmap[idx].key == key:
                self.hashmap[idx].key = -1
                self.size -= 1
                return True
            idx += 1
            idx = idx % self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        oldMap = self.hashmap
        self.capacity = self.capacity * 2
        self.hashmap = [None] * self.capacity
        self.size = 0
        for pair in oldMap:
            if pair and pair.key != -1:
                self.insert(pair.key, pair.val)

    def _hash(self, key) -> int:
        return key % self.capacity