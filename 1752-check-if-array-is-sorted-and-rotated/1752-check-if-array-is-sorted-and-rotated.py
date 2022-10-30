class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        noOfPeaks=0
        for i in range(1,n-1):
            if nums[i-1]<=nums[i]<=nums[i+1]:
                pass
            elif nums[i-1]>=nums[i]<=nums[i+1]:
                if noOfPeaks==0:
                    noOfPeaks+=1
            elif nums[i-1]<=nums[i]>nums[i+1]:
                noOfPeaks+=1
                if noOfPeaks>1:
                    return False
            else:
                return False
        return True if noOfPeaks==0 else nums[-1]<=nums[0]
                