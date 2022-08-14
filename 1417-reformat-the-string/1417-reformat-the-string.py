class Solution:
    def reformat(self, s: str) -> str:
        def lookForAlph(i,a):
            while i<n and not a[i].isalpha():
                i+=1
            if i<n and a[i].isalpha():
                return i
            return -1
        def lookForDig(i,a):
            while i<n and not a[i].isdigit():
                i+=1
            if i<n and a[i].isdigit():
                return i
            return -1
        def swapPos(i,j):
             a[i],a[j]=a[j],a[i]
        
        n=len(s)
        a=[s[i] for i in range(n)]
        for i in range(0,n-1,2):
            #print(i,a)
            if not a[i].isalpha():
                j=lookForAlph(i,a)
                if j==-1:
                    #print(a)
                    return ""
                swapPos(i,j)
            if i<n-1 and not a[i+1].isdigit():
                j=lookForDig(i+1,a)
                if j==-1:
                    #print(a)
                    return ""
                swapPos(i+1,j)
        if n%2==1 and a[-1].isdigit():
            a.insert(0,a.pop())
        #print(n,a)
        return ''.join(a)