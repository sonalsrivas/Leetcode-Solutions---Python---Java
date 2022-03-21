#User function Template for python3
class Solution:
    
    #Function to fill the array elements into a hash table 
    #using Quadratic Probing to handle collisions.
    def QuadraticProbing(self,hg, h, a, n):
        for i in a:
            c=i%h;
            #print(i,c);
            fst=c; flag=False; k=1
            while hg[c] not in (-1,i):
                c=(i+k*k)%h; 
                #print(c)
                k+=1
                
                #flag=False
                #if fst==c:
                
                #    break
                if k==h:
                    #flag=True
                    break
                #if c>=h:
                #    c=0
            #if flag:
            #    continue
            hg[c]=i
        return hg

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    
    while(T>0):
        
        
        hashSize=int(input())
        N=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        hash = [-1]*hashSize
        obj = Solution()
        obj.QuadraticProbing(hash, hashSize, arr, N)
        
        for i in hash:
            print(i,end=" ")
        print()
        T-=1


if __name__=="__main__":
    main()
# } Driver Code Ends