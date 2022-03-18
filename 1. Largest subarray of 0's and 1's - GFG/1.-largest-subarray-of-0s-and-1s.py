#User function Template for python3


# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray
# with equal 0s and 1s
class Solution:
    def maxLen(self,a, n):
        count=0
        ml=0
        mp={}
        for i in range(n):
            if a[i]==0:
                count+=1
            else:
                count-=1
            if count==0:
                ml=max(ml, i+1)
            if count in mp:
                ml=max(ml,i-mp[count])
            else:
                mp[count]=i
        return ml

#{ 
#  Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().maxLen(a, len(a))
    print(s)
# } Driver Code Ends