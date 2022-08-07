import string


class Trie:
    substrHashes = {}
    commons=set()
    def __init__(self, folder=['/']):
        self.folder = folder
        self.subfolderMap = {}
        self.markForDeletion = False
        self.hashedSubStructure = ''

    def add(self, newFolderPath):
        node = self
        for i, subfolderPath in enumerate(newFolderPath):
            if subfolderPath not in node.subfolderMap:
                node.subfolderMap[subfolderPath] = Trie(newFolderPath[:i + 1])
            node = node.subfolderMap[subfolderPath]

    def hashTheSubstructure(self):
        node = self
        for char in sorted(node.subfolderMap):
            node.hashedSubStructure += '-'+node.subfolderMap[char].hashTheSubstructure()+'/'
        #print(f"Node {node.folder} has hashed subtree structure : {node.hashedSubStructure}")

        if node.hashedSubStructure not in Trie.substrHashes or node.hashedSubStructure == '':
            Trie.substrHashes[node.hashedSubStructure] = node
        else:
            Trie.commons.add(node.hashedSubStructure)
            node.markForDeletion = True
            Trie.substrHashes[node.hashedSubStructure].markForDeletion = True
        return node.folder[-1] + node.hashedSubStructure


class Solution:
    def deleteDuplicateFolder(self, paths):
        n = len(paths)

        Trie.substrHashes = {}
        Trie.commons=set()

        folderNode = Trie()

        for i, path in enumerate(paths):
            folderNode.add(path)
        folderNode.hashTheSubstructure()

        #print(Trie.commons)
        res = []

        def DFS(node):
            if node.folder[-1] != '/' and not node.markForDeletion:
                res.append(node.folder)
            for child in node.subfolderMap.values():
                if not child.markForDeletion:
                    DFS(child)

        DFS(folderNode)
        return res