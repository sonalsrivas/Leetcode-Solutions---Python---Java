class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        temp=sorted(nums2, reverse=True)
        return sum(nums1[i]*temp[i] for i in range(len(nums1)))