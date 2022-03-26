 #User function Template for python3
from collections import Counter as C
class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,a, n):
        #d=C(a); 
        a.sort()
        l=a[0]; r=a[0]; p=a[0]; m=0
        for i in a:
            if p+1==i: # i exists in A
                #if p+1==i: # if previous int is des.
                r=i
            elif p==i:
                pass
            else: # trail broken if once then l needs to be changed
                m=max(m,r-l+1)
                l=i
            p=i
        m=max(m,r-l+1)
        return m 
                    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends