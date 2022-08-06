class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        
        noOfMissingNumsInList=nums[right]-nums[left]-(right-left)
        
        if noOfMissingNumsInList<k:
            return nums[right]+k-noOfMissingNumsInList
        
        while left<right-1:
            mid=(left+right)//2
            noOfMissingNumsBtwLM=nums[mid]-nums[left]-(mid-left)
            
            if noOfMissingNumsBtwLM>=k:
                right=mid
            else:
                k-=noOfMissingNumsBtwLM
                left=mid
        
        return nums[left]+k