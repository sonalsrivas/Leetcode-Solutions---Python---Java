class Trie:
    
    def __init__(self,character=''):
        self.char=character
        self.children=OrderedDict()
        self.childLast=None
        
    def add(self, word,directedGraphAdjList,noOfIncoming):
        for c in word:
            if c not in self.children:
                newNode=Trie(c)
                self.children[c]=newNode
            elif (c in self.children and self.childLast!=c):
                return False
            self.childLast=c
            self=self.children[c]
        return True if not self.children else False


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        trie=Trie()
        directedGraphAdjList=defaultdict(list)
        noOfIncoming=defaultdict(int)
        visitedDict={}
        for word in words:
            addFlag=trie.add(word,directedGraphAdjList,noOfIncoming)
            if not addFlag:
                return ''
        
        def makeGraph(trieNode):
            prev=None
            for node in reversed(trieNode.children):
                visitedDict[node]="yetToProcess"
                if prev:
                    noOfIncoming[node]+=1
                    directedGraphAdjList[prev].append(node)
                prev=node
                makeGraph(trieNode.children[node])
        makeGraph(trie)
        
        def DFS(alphabet, res=''):
            visitedDict[alphabet]="processing"
            branchRes=''
            for nextNode in directedGraphAdjList[alphabet]:
                if visitedDict[nextNode]=="processing":
                    return 
                elif visitedDict[nextNode]=="processed":
                    continue
                newRes= DFS(nextNode,res)
                if not newRes:
                    return
                branchRes+=newRes
            visitedDict[alphabet]="processed"
            return res+branchRes+alphabet
        
        alienAlphbeticalOrder=''
        for alpha in visitedDict:
            if noOfIncoming[alpha]==0 or visitedDict[alpha]=='yetToProcess':
                res=DFS(alpha)
                if not res:
                    continue
                alienAlphbeticalOrder+=res
        
        for i in visitedDict:
            if visitedDict[i]=="processing":
                return ""
        
        return alienAlphbeticalOrder