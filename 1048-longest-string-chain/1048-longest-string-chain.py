class Solution:
    def __init__(self):
        self.maxLength = None

    def longestStrChain(self, words):
        self.maxLength = 1

        def DFSchain(word, chainLength=1):
            n = len(word)
            for i in range(n):
                nextWord = word[:i] + word[i + 1:]
                if nextWord in wordsVisited:
                    if not wordsVisited[nextWord]:
                        chainLength = max(chainLength, 1 + DFSchain(nextWord))
                    else:
                        chainLength = max(chainLength, 1 + wordsVisited[nextWord])

            wordsVisited[word] = chainLength
            return chainLength

        wordsVisited = {word: False for word in words}
        for word in wordsVisited:
            if not wordsVisited[word] and self.maxLength < len(word):
                self.maxLength = max(self.maxLength, DFSchain(word))
        return self.maxLength
