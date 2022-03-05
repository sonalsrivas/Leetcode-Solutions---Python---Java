class Solution:
    def xorOperation(self, n: int, s: int) -> int:
        a=[s+2*i for i in range(n)]
        x=0
        for i in a:
            x^=i
        return x