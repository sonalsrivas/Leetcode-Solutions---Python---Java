class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i=0
        n=len(s)
        spaceLen=len(spaces)
        k=0
        result=""
        while i<n:
            while i<n and ((k<spaceLen and i!=spaces[k]) or k==spaceLen):
                result+=s[i]
                i+=1
            if k<spaceLen and i==spaces[k]:
                result+=" "
                k+=1
        return result
        