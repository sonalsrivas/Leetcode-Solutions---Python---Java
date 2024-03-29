class Solution:
    def climbStairs(self, n: int) -> int:
        noOfWaysToGetToStep1before=1
        noOfWaysToGetToStep2before=0
        for stepCurrent in range(1,n+1):
            noOfWaysToGetToStepcurrent = noOfWaysToGetToStep1before + noOfWaysToGetToStep2before
            noOfWaysToGetToStep1before, noOfWaysToGetToStep2before = noOfWaysToGetToStepcurrent, noOfWaysToGetToStep1before
        return noOfWaysToGetToStepcurrent