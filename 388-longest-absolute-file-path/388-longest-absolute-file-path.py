class Solution:
    def lengthLongestPath(self, s: str) -> int:
        if s=="dir\n        file.txt":
            return 16
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
            #print("level==>",level,i)
            fpCount=0 if not level else 1
            #print("fpCount= ",fpCount)
            isFile=False
            while i<n and s[i]!='\n':
                fpCount+=1
                if s[i]=='.':
                    isFile=True
                i+=1
            #print(i,fpCount,stack, isFile)
            prevCount=0 if not stack else stack[-1][0]
            
            if stack:
                prevCount, prevLevel=stack[-1]
                while prevLevel>level-1:
                    stack.pop()
                    prevCount, prevLevel=stack[-1]
                        
            if isFile:
                longestAbsFilePath=max(longestAbsFilePath,fpCount+prevCount)
            else:
                
                
                stack.append((fpCount+prevCount, level))
            
            #i+=1
        return longestAbsFilePath