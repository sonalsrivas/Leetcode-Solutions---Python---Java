class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        top=-1
        stackMinimumOnRight=[0]
        n=len(prices)
        for i in range(n-1,-1,-1):
            if stackMinimumOnRight[top] <= prices[i]:
                discount=stackMinimumOnRight[top]
            else:
                while stackMinimumOnRight[top] > prices[i]:
                    stackMinimumOnRight.pop()
                discount=stackMinimumOnRight[top]
            stackMinimumOnRight.append(prices[i])
            prices[i]-= discount
        return prices
'''

closest on the right index which has smaller or equal value


  v
8 4 6 2 3
        ^  
4 2 2 0 0 -> smaller to my right
4 2 4 2 3 -> difference between org price and discount


4
2
3


8 7 6 2 3


6
2
3

'''