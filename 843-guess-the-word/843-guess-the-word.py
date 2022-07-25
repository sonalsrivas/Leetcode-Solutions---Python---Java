# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, w: List[str], master: 'Master') -> None:
        #w=wordlist
        random.shuffle(w)
        def exactMatch(randomGuess, word):
            return sum((a==b for a,b in zip(randomGuess, word)))
        for _ in range(10):
            randomWord=random.choice(w)
            randomGuessCloseness=master.guess(randomWord)
            w=[word for word in w if exactMatch(randomWord, word)==randomGuessCloseness]
            