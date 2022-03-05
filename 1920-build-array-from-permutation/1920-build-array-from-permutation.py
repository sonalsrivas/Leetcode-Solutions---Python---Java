class Solution:
    def buildArray(self, a: List[int]) -> List[int]:
        r=a[::]
        for i in range(len(a)):
            r[i]=a[a[i]]
        return r