class Solution:
    def missingElement(self, a: List[int], k: int) -> int:
        n=len(a)
        l=0
        r=n-1
        noOfMissingNumsInList=a[r]-a[l]-(r-l)
        if noOfMissingNumsInList<k:
            return a[r]+k-noOfMissingNumsInList
        while l<r-1:
            m=(l+r)//2
            noOfMissingNumsBtwLM=a[m]-a[l]-(m-l)
            if noOfMissingNumsBtwLM>=k:
                r=m
            else:
                k-=noOfMissingNumsBtwLM
                l=m
        return a[l]+k