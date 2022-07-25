class Solution:
    def longestStrChain(self, words):
        self.maxLength=1

        def DFSchain(word,chainLength=1):
            #self.maxLength=max(self.maxLength, chainLength)
            n=len(word)
            #print(word)
            #if self.maxLength>n:
            #    return
            for i in range(n):
                nextWord=word[:i]+word[i+1:]
                if nextWord in wordsVisited:
                    if not wordsVisited[nextWord]:
                        chainLength=max(chainLength, 1+DFSchain(nextWord))
                    else:
                        chainLength=max(chainLength, 1+wordsVisited[nextWord])
                        #chainLength+=wordsVisited[nextWord]
                    #if not wordsVisited[nextWord]:
            wordsVisited[word]=chainLength
            #print("word, chainLength => ",word, chainLength)
            return chainLength



        wordsVisited={word:False for word in words}
        for word in wordsVisited:
            if not wordsVisited[word] and self.maxLength<len(word):
                self.maxLength=max(self.maxLength, DFSchain(word))
        #print("------------------------------------")
        return self.maxLength