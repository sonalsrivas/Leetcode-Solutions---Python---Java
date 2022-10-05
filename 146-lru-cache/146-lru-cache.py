class LRUCache:

    def __init__(self, capacity: int):
        self.LRUCache=OrderedDict()
        self.cap=capacity
        self.occ=0

    def get(self, key: int) -> int:
        if key in self.LRUCache:
            self.updateKeyPosition(key)
            return self.LRUCache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache:
            self.LRUCache[key]=value
            self.updateKeyPosition(key)
        else:
            if self.occ>=self.cap:
                self.removeLeastRecentlyUsedKey()
            self.LRUCache[key]=value
            self.occ+=1
        
    def updateKeyPosition(self,key):
        self.LRUCache.move_to_end(key)
        
    def removeLeastRecentlyUsedKey(self):
        self.LRUCache.popitem(last=False)
        self.occ-=1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)