class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        negativeInfinity=-float('inf')
        maxSoFar=negativeInfinity
        maxThatEndsHere=negativeInfinity
        
        for number in nums:
            if maxThatEndsHere<0 and maxThatEndsHere<number:
                # if number is a positive integer and max ending at prev is actually a negative, then here is a chance for me reset my candidate subarray
                maxThatEndsHere=number
            else:
                maxThatEndsHere+=number
            
            maxSoFar = max(maxSoFar, maxThatEndsHere)
        
        return maxSoFar