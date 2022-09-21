class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        n=len(arr)
        mapElementFreq=Counter(arr)
        mapFreqUniq=defaultdict(int)
        for element, freq in mapElementFreq.items():
            mapFreqUniq[freq]+=1
        totalUniquePeople=len(mapElementFreq)
        for freq in sorted(mapFreqUniq.keys()):    
            for _ in range(mapFreqUniq[freq]):
                if k>=freq:
                    totalUniquePeople-=1
                    k-=freq
                else:
                    return totalUniquePeople
        return 0
'''

arr = 
[4,3,1,1,3,3,2], k = 3
mapElementFreq={4:1, 1:2, 3:3, 2:1}

mapFreqUniq={
freq:no of uniqueElements that have this freq
1:2, 2: 1, 3: 1
     ^
k=3 = 3-min(3, 1)=3-1=2
k=2 = 2-min(2, 1) = 2-1=1
k=1 = 1-min(1, 2)=1-1=0
totalPeople=n
for freq in sorted(mapFreqUniq.keys()):
    for _ in range(mapFreqUniq[freq]):
        removePeople=min(k, freq)
        totalPeople-=removePeople
        k-=removePeople
        if k==0:
            return totalPeople
for freq in mapElementFreq.values():

'''