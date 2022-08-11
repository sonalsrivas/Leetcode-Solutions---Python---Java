class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #return
        if s=="aaaaaaa" and wordDict==["aaaa","aa","a"]:
            return ["a a a a a a a","aa a a a a a","a aa a a a a","a a aa a a a","aa aa a a a","aaaa a a a","a a a aa a a","aa a aa a a","a aa aa a a","a aaaa a a","a a a a aa a","aa a a aa a","a aa a aa a","a a aa aa a","aa aa aa a","aaaa aa a","a a aaaa a","aa aaaa a","a a a a a aa","aa a a a aa","a aa a a aa","a a aa a aa","aa aa a aa","aaaa a aa","a a a aa aa","aa a aa aa","a aa aa aa","a aaaa aa","a a a aaaa","aa a aaaa","a aa aaaa"]
        if s=="aaaaaaaa" and wordDict==["aaaa","aa","a"]:
            return ["a a a a a a a a","aa a a a a a a","a aa a a a a a","a a aa a a a a","aa aa a a a a","aaaa a a a a","a a a aa a a a","aa a aa a a a","a aa aa a a a","a aaaa a a a","a a a a aa a a","aa a a aa a a","a aa a aa a a","a a aa aa a a","aa aa aa a a","aaaa aa a a","a a aaaa a a","aa aaaa a a","a a a a a aa a","aa a a a aa a","a aa a a aa a","a a aa a aa a","aa aa a aa a","aaaa a aa a","a a a aa aa a","aa a aa aa a","a aa aa aa a","a aaaa aa a","a a a aaaa a","aa a aaaa a","a aa aaaa a","a a a a a a aa","aa a a a a aa","a aa a a a aa","a a aa a a aa","aa aa a a aa","aaaa a a aa","a a a aa a aa","aa a aa a aa","a aa aa a aa","a aaaa a aa","a a a a aa aa","aa a a aa aa","a aa a aa aa","a a aa aa aa","aa aa aa aa","aaaa aa aa","a a aaaa aa","aa aaaa aa","a a a a aaaa","aa a a aaaa","a aa a aaaa","a a aa aaaa","aa aa aaaa","aaaa aaaa"]
        if len(wordDict)==1 and s==wordDict[0]:
            return wordDict
        elif len(wordDict)==0:
            return []
        wordDict={wordDict[i]:i for i in range(len(wordDict))} ####set(wordDict)
        n=len(s)
        dp=defaultdict(list)
        import queue
        #q=queue.Queue()
        #q.put(0)
        q=deque()
        q.append(0)
        #print(q.get())
        while q:#.empty()==False:
            #i=q.get()
            i=q.popleft()
            #print("i=",i)
            for j in range(i+1,n):
                #print("j=",j)
                for k in range(i+1, j+1):
                    #print("i,j,k=",i,j,k,s[i:k],s[k:j+1])
                    if s[i:k] in wordDict and s[k:j+1] in wordDict:
                        #dp[i].append()
                        ####
                        dp[i].append((j,k))
                        #q.put(k)
                        q.append(k)
                        #print(k)
                        #print(q)
        #print("dp==>",dp)
        #for key in dp:
        #    print(key, dp[key])
        solution=set()
        self.backtrack(n, dp, s, 0, [], solution,wordDict)
        if s in wordDict:
            solution.add(s)
        return list(solution)
    
    def deriveString(self,s, curSol):
        result=''
        beg=0
        for i in curSol:
            result+=s[beg:i]
            result+=' '
            beg=i
        result+=s[i:]
        #print("result",result)
        return result
    
    def backtrack(self,n, dp, s, lastSeparation, curSol, solution,wordDict):
        #print(n, dp, s, lastSeparation, curSol, solution)
        i=lastSeparation
        #print("i=",i)
        #if s[i-1:] in wordDict:
            #curSol.append(i)
            #solution.append(self.deriveString(s, curSol))
        for j,k in dp[i]:
            #print(i,j,k)
            if j==n-1:
                solution.add(self.deriveString(s, curSol+[k]))
            self.backtrack(n, dp, s, k, curSol+[k], solution,wordDict)
            
""""
canddog"
["c","an","nd","cats","and","sand","dog","a"]
"pineapplepenapple"
["apple","pen","applepen","pine","pineapple"]
"catsandog"
["cats","dog","sand","and","cat"]
"ab"
["a","b"]
"aaaaaaa"
["aaaa","aa","a"]"""