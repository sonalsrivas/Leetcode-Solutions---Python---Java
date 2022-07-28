class Solution:
    def minPartitions(self, n: str) -> int:
        a=[int(i) for i in n] #list(map(int, n.split("")))
        #min_=min(a)
        max_=max(a)
        #if min_==0:
        #    return max_
        return max_