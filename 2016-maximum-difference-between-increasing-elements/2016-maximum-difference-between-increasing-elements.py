class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        stack=[]
        maxDiffFound=-1
        for element in nums:
            while stack and stack[-1]>element:
                stack.pop()
            if not stack :
                stack.append(element)
                
            elif stack[-1]<element:
                stack.append(element)
                maxDiffFound=max(maxDiffFound, stack[-1]-stack[0])
            
        return maxDiffFound
            
'''


4
1


=4
'''