class Trie:
    
    def __init__(self,character=''):
        self.char=character
        self.children=OrderedDict()
        self.childLast=None
        
    def add(self, word,directedGraphAdjList,noOfIncoming):
        for c in word:
            if c not in self.children:# or self.children[-1][0]!=c:
                newNode=Trie(c)
                self.children[c]=newNode
            elif (c in self.children and self.childLast!=c):
                return False
            #if self.childLast:
                
            self.childLast=c
            self=self.children[c]
        return True if not self.children else False#True

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
            print("trieNode.char=> ",trieNode.char)
            prev=None
            for node in reversed(trieNode.children):
                visitedDict[node]="yetToProcess"
                #print(prev,node)
                if prev:
                    noOfIncoming[node]+=1
                    directedGraphAdjList[prev].append(node)
                prev=node
                makeGraph(trieNode.children[node])
        makeGraph(trie)
        def DFS(alphabet, res=''):
            #print("Beigninng of dfs funct::::  DFS ka res  ",res,alphabet)
            visitedDict[alphabet]="processing"
            #res+=alphabet
            branchRes=''
            for nextNode in directedGraphAdjList[alphabet]:
                if visitedDict[nextNode]=="processing":
                    #print("returning bare")
                    return 
                elif visitedDict[nextNode]=="processed":
                    continue
                newRes= DFS(nextNode,res)
                if not newRes:
                    return
                branchRes+=newRes
            visitedDict[alphabet]="processed"
            #print("## DFS ka res  ",res,alphabet)
            return res+branchRes+alphabet
        alienAlphbeticalOrder=''
        #print(noOfIncoming, directedGraphAdjList,alienAlphbeticalOrder,visitedDict)
        for alpha in visitedDict:
            if noOfIncoming[alpha]==0 or visitedDict[alpha]=='yetToProcess':
                res=DFS(alpha)
                #print("DFS ka res ---->  ",res,"   for alpha,..", alpha)
                if not res:
                    continue
                alienAlphbeticalOrder+=res
        print(noOfIncoming, directedGraphAdjList,alienAlphbeticalOrder,visitedDict)
        for i in visitedDict:
            if visitedDict[i]=="processing":
                return ""
        return alienAlphbeticalOrder