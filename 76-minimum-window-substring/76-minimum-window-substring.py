from collections import Counter


class Solution:
    def minWindow(self, s,a):
        
        def shortestPossibleStart(start,end):
            while start<end and (s[start] not in mapArrVisited or mapArrVisited[s[start]]<0) :
                if s[start] in mapArrVisited:
                    mapArrVisited[s[start]]+=1
                start+=1
            return start
        
        def addToResList(start, end):
            resList.append(s[start:end+1])
        
        def removeStartChar(start):   
            # everything is there in substring .. = mapArrVisited[char]=0, more=>-1, less=> +1
            if s[start] in mapArrVisited:
                mapArrVisited[s[start]]+=1
            start+=1
            return start
        
        def fixNewStart(start,end):
            while start<end and (s[start] not in mapArrVisited or mapArrVisited[s[start]]<0):
                start=removeStartChar(start)
            return start
            
        start=-1
        n=len(s)

        resList=[]
        mapArrVisited=Counter(a)
        freqReq=Counter(a)
        for end in range(n):
            character=s[end]
            if start!=-1:
                currentLength=end-start+1
            else:
                currentLength=n
            
            if character in mapArrVisited:
                mapArrVisited[character]-=1
                if start==-1:
                    start=end
                start=shortestPossibleStart(start,end)
                
                currentLength=end-start+1
                if not any(filter(lambda x: x>0,mapArrVisited.values())): #and 
                    addToResList(start, end)
                    
                    start=removeStartChar(start)
                    
                    start=fixNewStart(start,end)
                    
        smallestSubstring=s
        flag=False
        for sub in resList:
            if len(sub)<=len(smallestSubstring):
                smallestSubstring=sub
                flag=True
        return smallestSubstring if flag else ''