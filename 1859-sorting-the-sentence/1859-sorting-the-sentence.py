class Solution:
    def sortSentence(self, s: str) -> str:
        d={}
        word=''
        nm=0; m=0
        for i in s:
            if i!=" ":
                
                if i.isdigit():
                    nm*=10
                    nm+=int(i)
                else:
                    word+=i
            else:
                d[nm]=word
                m=max(m,nm)
                word=''
                nm=0
        d[nm]=word
        m=max(m,nm)
        #print(d)
        l=[d[i] for i in range(1,m+1)]
        return ' '.join(l)