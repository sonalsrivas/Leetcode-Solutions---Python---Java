class Solution:
    def makePalindrome(self, s: str) -> bool:
        diffCount=0
        for i in range(len(s)//2):
            b=s[i]
            d=s[-i-1]
            if b!=d:
                diffCount+=1
            if diffCount>2:
                return False
        return True