class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mapDigSumNumList = defaultdict(list)
        maxDigitSum=0
        for number in nums:
            digitsSum=self.findDigitsSum(number)
            mapDigSumNumList[digitsSum].append(number)
        
        largestSum=-1
        for digitsSum in sorted(mapDigSumNumList.keys(), reverse=True):
            
            numList=sorted(mapDigSumNumList[digitsSum])
            if len(numList)>1:
                largestSum = max(largestSum, numList[-1]+numList[-2])
            
        return largestSum
    def findDigitsSum(self,num):
        sum=0
        while num>0:
            sum+=num%10
            num//=10
        return sum