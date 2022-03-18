#User function Template for python3

# A[] : the input array of positive integers
# N : size of the array arr[]
# X : the required sum
from collections import Counter as F
class Solution:
    def keypair(self,a , n, x):
        s=F(a)
        for i in a:
            s[i]-=1
            if x-i in s and (x-i!=i or ( (x-i)==i and s[x-i]>-0)):
                return True
            s[i]+=1
        return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n,x=list(map(int,input().split()))
    a=list(map(int,input().split()))
    sln=Solution().keypair(a,n,x)
    if(sln):
        print("Yes")
    else:
        print("No")
# } Driver Code Ends