class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        mapFreq=Counter(nums)
        count=0
        for i in nums:
            if mapFreq[i]>0:
                mapFreq[i]-=1
                if k-i in mapFreq and mapFreq[k-i]>0:
                    count+=1
                    mapFreq[k-i]-=1
                    #print(mapFreq, i, k-i, count)
        return count