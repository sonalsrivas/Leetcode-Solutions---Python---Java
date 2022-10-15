from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapElementFrequency = Counter(nums)
    
        maxFreq=0
        minFreq=len(nums)
        mapFrequencyElementlist = defaultdict(list)
        for element, frequency in mapElementFrequency.items():
            mapFrequencyElementlist[frequency].append(element)
            maxFreq=max(maxFreq, frequency)
            minFreq=min(minFreq, frequency)
        
        listTopKFrequentElements=[]
        for freq in range(maxFreq, minFreq-1, -1):
            for element in mapFrequencyElementlist[freq]:
                listTopKFrequentElements.append(element)
                k-=1
            if k==0:
                break
        
        return listTopKFrequentElements