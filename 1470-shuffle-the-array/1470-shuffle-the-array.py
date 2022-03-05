class Solution:
    def shuffle(self, a: List[int], n: int) -> List[int]:
        r=[0]*2*n
        for i,j in zip(range(0,2*n,2), range(n)):
            r[i]=a[j]
        for i,j in zip(range(1,2*n,2), range(n,2*n)):
            r[i]=a[j]
        return r