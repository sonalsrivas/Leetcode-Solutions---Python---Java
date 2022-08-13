class Solution:
    def countPoints(self, rings: str) -> int:
        d={str(i):[0,0,0] for i in range(10)}
        i=0
        while i<len(rings):
            if rings[i]=="R":
                d[rings[i+1]][0]=1
            if rings[i]=="G":
                d[rings[i+1]][1]=1
            if rings[i]=="B":
                d[rings[i+1]][2]=1
            i+=2
        count=0
        for i in d:
            if d[i]==[1,1,1]:
                count+=1
        return count