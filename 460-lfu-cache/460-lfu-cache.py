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
        if not self.mapFreqToKeysList[self.minimumFrequency]:
            nextMinimum = 1
            while nextMinimum <= 2*10**5 and not self.mapFreqToKeysList[nextMinimum]:
                nextMinimum += 1
            self.minimumFrequency = nextMinimum
        #print("===============", self.minimumFrequency)

    def put(self, key, value):
        if self.capacity==0:
            return
        #print("PUTTING-- key, value = ",key, value)
        #print("self.mapFreqToKeysList => ",self.mapFreqToKeysList)
        #print("self.LFUCacheStore => ",self.LFUCacheStore)
        if key in self.LFUCacheStore:
            # updating map of key value
            prevFrequency = self.LFUCacheStore[key][1]
            self.LFUCacheStore[key] = [value, prevFrequency + 1]

            # updating map of freq
            #print("self.mapFreqToKeysList => ",self.mapFreqToKeysList)
            self.findNextMinimumFrequency()
            #print("popping offffffff. ", prevFrequency, self.mapFreqToKeysList[prevFrequency])
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
                #print("self.mapFreqToKeysList => ",self.mapFreqToKeysList)
                #print("self.LFUCacheStore => ",self.LFUCacheStore)
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
        #print("FINAL ::: self.mapFreqToKeysList => ",self.mapFreqToKeysList)
        #print("FINAL ::: self.LFUCacheStore => ",self.LFUCacheStore)

    def get(self, key):
        if self.capacity==0:
            return -1
        #print("GETTING-- key = ",key,"The MAP is: ")
        if key in self.LFUCacheStore :
            self.put(key, self.LFUCacheStore[key][0])
            return self.LFUCacheStore[key][0]
        else:
            return -1


