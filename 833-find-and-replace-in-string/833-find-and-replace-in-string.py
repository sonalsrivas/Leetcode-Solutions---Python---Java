class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def findReplaceString(self, string: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        a = [Node(c) for c in string]  # string index with node object
        n = len(string)
        for i in range(n - 1):
            a[i].next = a[i + 1]

        for index, src, targ in zip(indices, sources, targets):
            # confirm that the substring exists at the index
            substringDoesNotOccur = False
            tempInd = index
            for s in src:
                if tempInd >= n or s != string[tempInd]:
                    substringDoesNotOccur = True
                    break
                tempInd += 1

            if substringDoesNotOccur:
                continue

            a[index].val = targ

            # adjust for non-starting characters in teh substring
            endIndexOfSubstring = tempInd

            if endIndexOfSubstring < n:
                a[index].next = a[endIndexOfSubstring]
            else:
                a[index].next = None

        finalString = ""
        node = a[0]
        while node:
            finalString += node.val
            node = node.next
        return finalString
