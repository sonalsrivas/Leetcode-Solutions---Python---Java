#User function Template for python3

def max_sum(a,n):
    s=sum(a)
    f=0
    
    for i in range(n):
        f+=a[i]*i
    m=f
    for i in range(n-1, 0,-1):
        t=f+s-a[i]*n
        f=t
        m=max(m,t)
    return m
#{ 
#  Driver Code Starts
#Initial Template for Python 3


    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr,n))
# } Driver Code Ends