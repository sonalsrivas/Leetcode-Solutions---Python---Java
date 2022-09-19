from collections import Counter


class Solution:
    def minWindow(self, s,a):
        
        def shortestPossibleStart(start,end):
            while start<end and (s[start] not in mapArrVisited or mapArrVisited[s[start]]<0) :
                if s[start] in mapArrVisited:
                    mapArrVisited[s[start]]+=1
                start+=1
            return start
        
        def addToResList(start, end, p,q):
            if end-start<q-p:
                p,q=start,end
            return p,q
            
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

        p,q=-n,n
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
                    p,q=addToResList(start, end,p,q)
                    
                    start=removeStartChar(start)
                    
                    start=fixNewStart(start,end)
                    
        return s[p:q+1] if q-p<n else ''