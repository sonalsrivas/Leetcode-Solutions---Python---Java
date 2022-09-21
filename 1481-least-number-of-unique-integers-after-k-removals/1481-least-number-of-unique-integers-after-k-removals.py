class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        n=len(arr)
        mapElementFreq=Counter(arr)
        print("mapElementFreq=> ",mapElementFreq)
        mapFreqUniq=defaultdict(int)
        for element, freq in mapElementFreq.items():
            mapFreqUniq[freq]+=1
        print("mapFreqUniq=> ",mapFreqUniq)
        totalUniquePeople=len(mapElementFreq)
        for freq in sorted(mapFreqUniq.keys()):
            
            for _ in range(mapFreqUniq[freq]):
                print("freq, _, k  => \t ",freq, _,k)
                if k>=freq:
                    totalUniquePeople-=1
                print(k>=freq, " \t totalUniquePeople = ", totalUniquePeople)
                removePeople=min(k, freq)
                #totalPeople-=removePeople
                k-=removePeople
                if k==0:
                    return totalUniquePeople
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