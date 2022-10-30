class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapOrderIndex={order[i]:i for i in range(len(order))}
        n=len(words)
        breakers=[0]*n
        
        def checkOrderInAlphabet(previousWordChar, wordChar):
            return mapOrderIndex[previousWordChar] < mapOrderIndex[wordChar]
        
        for position in range(20):
            previousWordChar = ''
            for word_i, word in enumerate(words):
                if len(word)<=position:
                    if breakers[word_i]==0 and len(words[word_i-1])>position:
                        return False
                    continue
                if previousWordChar != word[position]:
                    if breakers[word_i]==0:
                        if previousWordChar:
                            result=checkOrderInAlphabet(previousWordChar, word[position])
                            if not result:
                                return False
                    breakers[word_i]=1
                previousWordChar = word[position]
        return True
'''

1. store the index of each alpha 
2. traverse each position 
'''