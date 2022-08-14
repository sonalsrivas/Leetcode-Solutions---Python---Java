class Solution:
    def findKthPositive(self, a: List[int], k: int) -> int:
        low=0
        missingNums=0
        for i in a:
            pmN=missingNums
            if low+1<i:
                missingNums+=i-low-1
            if missingNums>=k:
                return low+k-pmN
            low=i
        return low+k-missingNums