from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.maxCap= capacity
        self.LRU=OrderedDict()   # key : value
        self.curCap=0
    def get(self, key):
        if key in self.LRU:
            self.LRU.move_to_end(key)
            val=self.LRU[key]
            #del self.LRU[key]
            #self.LRU[key]=val
            return val
        else:
            return -1
    def put(self, key, value):
        if key in self.LRU:
            self.LRU.move_to_end(key)
            self.LRU[key]=value
            return 
        if self.curCap == self.maxCap:
            self.LRU.popitem(last=False)
            self.curCap-=1
        self.LRU[key]=value
        self.curCap+=1