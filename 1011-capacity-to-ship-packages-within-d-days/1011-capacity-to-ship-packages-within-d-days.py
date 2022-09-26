class Solution:
    def shipWithinDays(self, weights, days):

        def findNoOfDivisionsOfSubarray(maxSubarraySum):
            noOfDivs=1; currentSubarraySum=0
            for weight in weights:
                currentSubarraySum += weight
                if currentSubarraySum > maxSubarraySum:
                    noOfDivs+=1
                    currentSubarraySum=weight
            return noOfDivs

        def binarySearch(left, right, days):
            while left<right:
                mid=(left+right)//2
                noOfDivisionsOfSubarray= findNoOfDivisionsOfSubarray(mid)
                if noOfDivisionsOfSubarray <= days:
                    right=mid
                else:
                    left=mid+1
            return left

        left, right = max(weights), sum(weights)

        return binarySearch(left, right, days)