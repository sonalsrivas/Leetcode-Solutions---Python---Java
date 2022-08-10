import re
class Solution:
    def expand(self, s: str) -> List[str]:
        ans=[]
        a=[]
        def divide(s,a,n):
            i=0
            while i<n:
                if s[i]=='{':
                    i+=1
                    temp=''
                    while s[i]!='}':
                        temp+=s[i]
                        i+=1
                    a.append(tuple(sorted(temp.split(','))))
                    i+=1
                if i<n and s[i]!='{':
                    a.append(s[i])
                    i+=1
        def backtrack(a,i,n,word):
            while i<n and isinstance(a[i], str):
                word+=a[i]
                i+=1  
            else:
                if i>=n:
                    ans.append(word)
                    return
                for char in a[i]:
                    backtrack(a,i+1,n,word+char)
                
        divide(s,a,len(s))
        backtrack(a,0,len(a), '')
        return ans