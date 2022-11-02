class Trie:

    def __init__(self,car=''):
        
        self.character=car
        self.children=dict()        # char:TrieNode
        self.word=False
        self.parent=None

    def insert(self, word: str) -> None:
        
        root=self
        for w in word:
            if w in root.children:
                root=root.children[w]
            else:
                root.children[w]=Trie(w)
                root.children[w].parent=root
                root=root.children[w]
            
        root.word=True
        
    def delete(self, word):
        for c in word[::-1]:
            if c in self.parent.children and self.parent.children[c].children=={}:
                self.parent.children.pop(c)
                
            if len(self.parent.children)>=1:
                return


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m=len(board)
        n=len(board[0])
        neighbours=((0,1),(0,-1),(-1,0),(1,0))
        trie=Trie()
        headTrie=trie
        
        for word in words:
            trie.insert(word)
            
        
        wordsSet=set(words)
        result=[]
        def DFS(i,j,trie, word):
            flagTrieWordFound=False
            
            if trie.word and word in wordsSet:
                result.append(word)
                flagTrieWordFound=True
                wordsSet.remove(word)
            
            for x,y in neighbours:
                x+=i
                y+=j
                if -1<x<m and -1<y<n and board[x][y] in trie.children:
                    currentCharacter=board[x][y]
                    board[x][y]='-'
                    DFS(x,y,trie.children[currentCharacter], word+currentCharacter)
                    board[x][y] = currentCharacter
            
            if flagTrieWordFound:
                trie.delete(word)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in headTrie.children: 
                    currentCharacter=board[i][j]
                    board[i][j]='-'
                    DFS(i,j,headTrie.children[currentCharacter], currentCharacter)
                    board[i][j]=currentCharacter
                    
        return result