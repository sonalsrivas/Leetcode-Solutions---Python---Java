class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y=0,0
        pd=set()
        pd.add((x,y))
        for c in path:
            if c=='N':
                y+=1
            elif c=='S':
                y-=1
            elif c=='E':
                x+=1
            elif c=='W':
                x-=1
            if (x,y) in pd:
                return True
            pd.add((x,y))
        return False