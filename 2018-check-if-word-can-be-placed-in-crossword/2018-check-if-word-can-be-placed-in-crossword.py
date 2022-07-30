class Solution:
    def placeWordInCrossword(self, a: List[List[str]], w: str) -> bool:
        
        preComp=set()
        
        def helper(a,w):
            m=len(a)
            n=len(a[0])
            wl=len(w)
            for i in range(m):
                j=0
                
                while j<n:
                    #print(i,j,a[i][j])
                    s=''       ##
                    while j<n and a[i][j]=='#':
                        j+=1
                    start=None
                    while (j<n and a[i][j]!="#"):
                        if not start:
                            start=(i,j)
                        #print("adding to s, this ", a[i][j])
                        s+=a[i][j] if a[i][j]!=' ' else '.'
                        #print("now s is ", s)
                        #a[i][j]='#'
                        j+=1
                    else:
                        if start and j-start[1]==wl:
                            preComp.add((start, j-start[1], s))
            #print("after horizontal : ",preComp)
            for j in range(n):
                i=0
                
                while i<m:
                    #print(i,j,a[i][j])
                    s=''       ##
                    while i<m and a[i][j]=='#':
                        i+=1
                    start=None
                    while (i<m and a[i][j]!="#"):
                        if not start:
                            start=(i,j)
                        #print("adding to s, this ", a[i][j])
                        s+=a[i][j] if a[i][j]!=' ' else '.'
                        #print("now s is ", s)
                        a[i][j]='#'
                        i+=1
                    else:
                        if start and i-start[0]==wl:
                            preComp.add((start, i-start[0], s))
        helper(a,w)
        #print("FINAL : ",preComp)
        for coord,length, string in preComp:
            if re.match(string, w) or re.match(string, w[::-1]):
                #print(string,w)
                return True
        return False
    def helper(self,a,w):
        m=len(a)
        n=len(a[0])
        wl=len(w)
        for i in range(m):
            j=0
            while j<n:
                while j<n and a[i][j]=='#':
                    j+=1
                wi=0
                while (j<n and a[i][j]!="#" and wi<wl):
                    if a[i][j]!=" " and a[i][j]!=w[wi]:
                        j+=1
                        break
                    j+=1
                    wi+=1
                else:
                    if wi==wl:
                        print("@@@ ",a,w,wl,wi,i,j,a[i][j])
                        return True
        for j in range(n):
            i=0
            while i<n:
                while i<n and a[i][j]=='#':
                    i+=1
                wi=0
                while (i<n and a[i][j]!="#"):
                    print(i,wi,a[i][j])
                    if a[i][j]!=" " and wi<wl and a[i][j]!=w[wi]:
                        i+=1
                        break
                    i+=1
                    wi+=1
                else:
                    if wi==wl:
                        print("%%#&",a,w,wl,wi,i,j)
                        return True
        return False