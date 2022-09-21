class Solution:
    def climbStairs(self, n: int) -> int:
        noOfWaysToGetToStep1before=1
        noOfWaysToGetToStep2before=0
        noOfWaysToGetToStepcurrent=1
        for stepCurrent in range(1,n+1):
            print(noOfWaysToGetToStep2before, noOfWaysToGetToStep1before, noOfWaysToGetToStepcurrent)
            noOfWaysToGetToStepcurrent = noOfWaysToGetToStep1before + noOfWaysToGetToStep2before
            noOfWaysToGetToStep1before, noOfWaysToGetToStep2before = noOfWaysToGetToStepcurrent, noOfWaysToGetToStep1before
        return noOfWaysToGetToStepcurrent