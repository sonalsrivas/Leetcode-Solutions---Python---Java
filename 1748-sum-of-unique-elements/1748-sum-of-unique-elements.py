class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum=0
        mapNumsFreq=Counter(nums)
        for i in mapNumsFreq:
            if mapNumsFreq[i]==1:
                sum+=i
        return sum