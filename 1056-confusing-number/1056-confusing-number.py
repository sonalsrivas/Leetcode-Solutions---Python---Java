class Solution:
    def confusingNumber(self, n: int) -> bool:
        grammar={'6':'9','9':'6','1':'1','0':'0','8':'8'}
        a=[]
        n=str(n)
        for i in n[::-1]:
            if i in grammar:
                a.append(grammar[i])
            else:
                return False
        a=''.join(a)
        return a!=n