class Solution:
    def myPow(self, number: float, power: int) -> float:
        if power==0:
            return 1
        halfPow=self.myPow(number, int(power/2))
        if power%2==0:
            return halfPow*halfPow
        if power>0:
            return halfPow*halfPow*number
        return halfPow*halfPow/number