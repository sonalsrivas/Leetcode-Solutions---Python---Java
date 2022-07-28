class Solution:
    def decodeString(self, s: str) -> str:
        s='['+s+']'
        n=len(s)
        
        def helper(s, i, n):
            string=''
            c=0
            ori_i=i
            num=0
            while i<n:
                if s[i]=='[':
                    c+=1
                    if i>ori_i:
                        childSt,i=helper(s,i,n)
                        string+=childSt*(num if num else 1)
                        num=0
                    else:
                        i+=1
                
                elif s[i].isdigit():
                    num*=10
                    num+=int(s[i])
                    i+=1
                
                elif s[i].isalpha():
                    string+=s[i]
                    i+=1
                
                elif s[i]==']':
                    c-=1
                    if c==0:
                        return string, i
                    i+=1
                    
            return string,i
            
        res, i=helper(s, 0, n)
        return res