class Solution:
    def createTargetArray(self, a: List[int], i: List[int]) -> List[int]:
        r=[]
        for j in range(len(a)):
            r.insert(i[j],a[j])
        return r