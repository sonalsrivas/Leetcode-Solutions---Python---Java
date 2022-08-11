class Solution:
    def lengthLongestPath(self, s: str) -> int:
        n=len(s)
        longestAbsFilePath=0
        stack=[(0,-1)]
        i=0
        while i<n:
            level=0
            if i<n and s[i]=='\n':
                i+=1
                while s[i]=='\t':
                    level+=1
                    i+=1
            
            fpCount=0 if not level else 1
            
            isFile=False
            while i<n and s[i]!='\n':
                fpCount+=1
                if s[i]=='.':
                    isFile=True
                i+=1
            
            if stack:
                prevCount, prevLevel=stack[-1]
                while prevLevel>level-1:
                    stack.pop()
                    prevCount, prevLevel=stack[-1]
                        
            if isFile:
                longestAbsFilePath=max(longestAbsFilePath,fpCount+prevCount)
            else:
                stack.append((fpCount+prevCount, level))
            
        return longestAbsFilePath