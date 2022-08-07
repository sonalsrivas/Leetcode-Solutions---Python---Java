class Trie:
    subStringHashes = {}

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
            node.hashedSubStructure += '-' + node.subfolderMap[char].hashTheSubstructure() + '/'

        if node.hashedSubStructure not in Trie.subStringHashes or node.hashedSubStructure == '':
            Trie.subStringHashes[node.hashedSubStructure] = node
        else:
            node.markForDeletion = True
            Trie.subStringHashes[node.hashedSubStructure].markForDeletion = True
        return node.folder[-1] + node.hashedSubStructure


class Solution:
    def deleteDuplicateFolder(self, paths):
        n = len(paths)

        Trie.subStringHashes = {}

        folderNode = Trie()

        for i, path in enumerate(paths):
            folderNode.add(path)
        folderNode.hashTheSubstructure()

        res = []

        def DFS(node):
            if node.folder[-1] != '/' and not node.markForDeletion:
                res.append(node.folder)
            for child in node.subfolderMap.values():
                if not child.markForDeletion:
                    DFS(child)

        DFS(folderNode)
        return res