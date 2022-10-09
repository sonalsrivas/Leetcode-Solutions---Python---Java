from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, cap):
        self.capacity = cap
        self.LFUCacheStore = dict()
        self.mapFreqToKeysList = defaultdict(OrderedDict)
        self.minimumFrequency = 0
        self.occupiedSpace = 0

    def findNextMinimumFrequency(self):
        if self.mapFreqToKeysList:
            self.minimumFrequency=min(self.mapFreqToKeysList.keys())
        return

    def put(self, key, value):
        if self.capacity==0:
            return
        if key in self.LFUCacheStore:
            # updating map of key value
            prevFrequency = self.LFUCacheStore[key][1]
            self.LFUCacheStore[key] = [value, prevFrequency + 1]

            self.findNextMinimumFrequency()
            self.mapFreqToKeysList[prevFrequency].pop(key)#item(last=False)
            if not self.mapFreqToKeysList[prevFrequency]:
                del self.mapFreqToKeysList[prevFrequency]
            self.findNextMinimumFrequency()
            self.mapFreqToKeysList[prevFrequency + 1][key] = value

        else:

            # MY CAP increases!!!
            if self.occupiedSpace >= self.capacity:
                self.findNextMinimumFrequency()
                keyRemoved, valueRemoved = self.mapFreqToKeysList[self.minimumFrequency].popitem(last=False)
                if not self.mapFreqToKeysList[self.minimumFrequency]:
                    del self.mapFreqToKeysList[self.minimumFrequency]
                self.LFUCacheStore.pop(keyRemoved)
                self.findNextMinimumFrequency()

            # to check cap

            # if exceed: remove LFU
            #     if multiple: remove LRU
            # if not exceed: go ahead

            self.LFUCacheStore[key] = [value, 1]
            self.mapFreqToKeysList[1][key] = value
            self.minimumFrequency = 1
            self.occupiedSpace += 1
            
    def get(self, key):
        if self.capacity==0:
            return -1
        if key in self.LFUCacheStore :
            self.put(key, self.LFUCacheStore[key][0])
            return self.LFUCacheStore[key][0]
        else:
            return -1


