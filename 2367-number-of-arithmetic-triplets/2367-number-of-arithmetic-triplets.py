class Solution:
    def arithmeticTriplets(self, a: List[int], d: int) -> int:
        s=set(a)
        c=0
        for i in a:
            if i+d in s and i+2*d in s:
                c+=1
        return c