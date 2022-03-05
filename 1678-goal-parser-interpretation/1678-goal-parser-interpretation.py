class Solution:
    def interpret(self, c: str) -> str:
        s=''
        p=''
        for i in c:
            if i=='G':
                s+=i
            elif i==')':
                if p=='l':
                    s+='al'
                else:
                    s+='o'
            else:
                p=i
        return s