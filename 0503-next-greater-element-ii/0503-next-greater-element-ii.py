class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack = []; top=-1    
        # storing index rather tahn element in the stack
        resultArray = [None]*n*2
        
        nums=nums+nums
        stack=[]
        for i in range(2*n):
            if stack==[]:
                pass
            elif nums[stack[-1]]<nums[i]:
                while stack and nums[stack[-1]]<nums[i]:
                    resultArray[stack.pop()]=nums[i]
            stack.append(i)
            
        while stack:
            resultArray[stack.pop()]=-1
        return resultArray[:n]