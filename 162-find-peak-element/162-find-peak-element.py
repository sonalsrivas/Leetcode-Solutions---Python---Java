class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            # Looking for the left neighbour here.... right neighbour
            if (i-1==-1 or (nums[i-1] < nums[i])) and (i+1==n or (nums[i] > nums[i+1] ) ) :
                return i