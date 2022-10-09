class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        n=len(nums)
        left, right=0,n-1
        while left<right:
            mid=(left + right)//2
            print(left, mid, right, target)
            if nums[mid]==target or  nums[left]==target or  nums[right]==target :
                return True
            elif nums[mid] < target < nums[right]:
                left=mid+1
            elif nums[left]<target<nums[mid]:
                right=mid-1
            elif nums[left]<nums[mid]:
                left=mid+1
            elif nums[mid]<nums[right]:
                right=mid-1
            else:
                return self.search(nums[left:mid+1], target) or self.search(nums[mid+1:right], target)
        print(left, nums, target)
        return nums[left]==target