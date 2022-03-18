#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, a):
        sm=0
        res=0
        mp={}
        for i in range(n):
            sm+=a[i]
            if sm==0:
                res=max(res, i+1)
            if sm in mp:
                res=max(res, i-mp[sm])
            else:
                mp[sm]=i
        return res

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends