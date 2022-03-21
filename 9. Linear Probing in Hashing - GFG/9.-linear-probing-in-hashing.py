#User function Template for python3

class Solution:
    #Function to fill the array elements into a hash table 
    #using Linear Probing to handle collisions.
    def linearProbing(self,h, a, n):
        hg=[-1]*h
        for i in a:
            cd=i%h
            if hg[cd]==-1:
                hg[cd]=i
            else:
                k=0;flag=False
                while cd<h and hg[cd] not in (-1,i):
                    k+=1
                    if k>h:
                        flag=True
                        break
                    cd+=1
                    if cd==h:
                        cd=0
                if flag:
                    break
                hg[cd]=i
        return hg
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():
    T=int(input())
    
    while(T>0):
        
        hashSize=int(input())
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        hash = obj.linearProbing( hashSize, arr, sizeOfArray)
        
        for i in hash:
            print(i,end=" ")
        print()
        T-=1


if __name__=="__main__":
    main()
# } Driver Code Ends