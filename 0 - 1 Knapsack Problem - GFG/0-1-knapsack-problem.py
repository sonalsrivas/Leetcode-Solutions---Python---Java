#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp = [0 for i in range(W+1)]  # Making the dp array
 
        for i in range( n):  # taking first i elements
            for w in range(W, 0, -1):  # starting from back,so that we also have data of
                                    # previous computation when taking i-1 items
                if wt[i] <= w:
                    # finding the maximum value
                    dp[w] = max(dp[w], dp[w-wt[i]]+val[i])
            #print(dp)
        return dp[W]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends