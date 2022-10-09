class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroStart=-1
        for i in range(len(nums)):
            if nums[i]==0:
                if zeroStart==-1:
                    zeroStart=i
                continue
            if zeroStart!=-1:
                nums[i], nums[zeroStart]=nums[zeroStart], nums[i]
                zeroStart+=1
        
'''
[1,3,12,0,0]
          ^
        ^

[1,3,0,0,12]
         ^
     ^
 

'''