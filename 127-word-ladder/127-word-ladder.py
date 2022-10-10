import queue
class Solution:
    def ladderLength(self, beginWord: str, target: str, wordList: List[str]) -> int:
        mapWordVisited={word:0 for word in wordList}
        
        if target not in mapWordVisited:
            return 0
        q=queue.Queue()
        q.put((beginWord, 1))
        
        while not q.empty():
            word, steps=q.get()
            wordLen=len(word)
            for i in range(wordLen):
                currentCharacter=word[i]
                for alternativeCharacter in string.ascii_lowercase:
                    if currentCharacter == alternativeCharacter:
                        continue
                    
                    nextPossibleWord=word[:i]+alternativeCharacter+word[i+1:]
                    
                    if nextPossibleWord in mapWordVisited and mapWordVisited[nextPossibleWord]==0:
                        if nextPossibleWord==target:
                            return steps+1
                        q.put((nextPossibleWord, steps+1))
                        mapWordVisited[nextPossibleWord]=1
        return 0