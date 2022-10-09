class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxOnTheRightSide=-float('inf')
        maxProfitFound=0
        n=len(prices)
        for i in range(n-1, -1,-1):
            maxProfitFound=max(maxProfitFound,maxOnTheRightSide-prices[i])
            maxOnTheRightSide=max(maxOnTheRightSide, prices[i])
        return maxProfitFound
        
'''

[7,1,5,3,6,4]
 ^
 - 6 6 6 -  -


'''