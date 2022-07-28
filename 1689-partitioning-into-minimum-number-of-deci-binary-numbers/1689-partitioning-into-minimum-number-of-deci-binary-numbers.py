class Solution:
    def minPartitions(self, n: str) -> int:
        a=[int(i) for i in n]
        max_=max(a)
        return max_