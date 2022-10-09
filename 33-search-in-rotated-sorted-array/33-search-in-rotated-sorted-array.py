class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left, right=0,n-1
        while left<right:
            mid=(left + right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target <= nums[right]:
                left=mid+1
            elif nums[left]<=target<nums[mid]:
                right=mid-1
            elif nums[left]<=nums[mid]:
                left=mid+1
            else:
                right=mid-1
        return left if nums[left]==target else -1
                        
'''
[4,5,6,7,0,1,2]
 l     m.    r
 t < l < m > r

either my mid can be left of pivot of right
target>mid  ... 
    if pivot is left of mid, then target can lie right of mid or left of pivot
    if pivot is right of mid, then target can lie only between this mid and pivot ie. on right of mid
target<mid ...
    pivot is left of mid, then target can lie only between this mid and pivot ie. left of mid
    pivot is right of mid, then target can lie right of pivot and left of mid
    
How to know on which side pivot is?..
if right < mid then pvt on right of mid
if left > mid then pvt on left of mid
'''