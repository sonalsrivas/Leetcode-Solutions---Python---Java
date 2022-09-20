class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        maxFrequency=max(Counter(nums).values())
        if maxFrequency==1:
            return 1
        left, right,n=0,0,len(nums)
        mapFreq={}; curMaxFreq=0
        degreeOfArr=n
        for right in range(n):
            if nums[right] in mapFreq:
                mapFreq[nums[right]]+=1
                if mapFreq[nums[right]]>=maxFrequency:
                    # reduce from left
                    while nums[left]!=nums[right]:
                        mapFreq[nums[left]]-=1
                        left+=1
                    degreeOfArr=min(degreeOfArr, right-left+1)
            else:
                mapFreq[nums[right]]=1
                
        return degreeOfArr
            
"""
2 1
*
  ^
2:1, 1:1

1 2 2 3 1
  *     ^

mF=2

mapFreq={
xxx 1:1
2:2
3:1
1:1
}
"""