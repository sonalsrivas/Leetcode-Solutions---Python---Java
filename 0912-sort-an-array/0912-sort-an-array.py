class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mapElementFrequency = Counter(nums)
        minEle=min(nums)
        maxEle=max(nums)
        k=0
        for element in range(minEle, maxEle+1):
            if element in mapElementFrequency:
                while mapElementFrequency[element]>0:
                    mapElementFrequency[element]-=1
                    nums[k]=element
                    k+=1
        return nums