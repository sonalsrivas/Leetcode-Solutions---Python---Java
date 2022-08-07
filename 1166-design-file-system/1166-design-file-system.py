class Trie:
    def __init__(self, filePath='', value=''):
        self.filePath=filePath
        self.children={}  # {fileName : TrieNode , ...}
        self.value=value
    
    def add(self, file,val):
        res=Trie.checkIfValidPath(self, file)
        if res==False:
            return res
        parent, newFile=res
        if newFile in parent.children:
            return False
        newNode=Trie(file)
        parent.children[newFile]=newNode
        newNode.value=val
        return True
    
    def checkIfValidPath(node, filePath):
        filePath=filePath.split('/')
        probableNewFile=filePath[-1]
        for file in filePath[1:-1]:
            if not file in node.children:
                return False
            node=node.children[file]
        return node, probableNewFile
    
    
class FileSystem:

    def __init__(self):
        self.filesystem=Trie()

    def createPath(self, path: str, value: int) -> bool:
        return self.filesystem.add(path, value)

    def get(self, path: str) -> int:
        res=Trie.checkIfValidPath(self.filesystem, path)
        if res==False:
            return -1
        if res[1] not in res[0].children:
            return -1
        return res[0].children[res[1]].value


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)