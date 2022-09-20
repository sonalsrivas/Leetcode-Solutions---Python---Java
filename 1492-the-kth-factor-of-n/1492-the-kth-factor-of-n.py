class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        squareRoot=int(n**0.5)
        print("squareRoot = ",squareRoot)
        for i in range(1, squareRoot+1):
            if n%i==0:
                k-=1
            print(i,k)
            if k==0:
                return i
        if squareRoot*squareRoot==n:
            squareRoot-=1
        for i in range(squareRoot,0,-1):
            if n%i==0:
                i=n//i
                k-=1
            print("other  ",i,k)
            if k==0:
                return i
        return -1 