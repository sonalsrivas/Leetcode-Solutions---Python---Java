from collections import Counter as C
class Solution:
    def numIdenticalPairs(self, a: List[int]) -> int:
        d=C(a)
        c=0
        for i in d:
            c+=(d[i]*(d[i]-1))//2
        return c