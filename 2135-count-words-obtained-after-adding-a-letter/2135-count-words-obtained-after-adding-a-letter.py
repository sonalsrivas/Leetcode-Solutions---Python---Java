class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        count=0
        s=set()
        for word in startWords:
            wordMask=0
            for c in word:
                wordMask^=1<<(ord(c)-ord('a'))
            s.add(wordMask)
        
        for word in targetWords:
            wordMask=0
            for c in word:
                wordMask^=1<<(ord(c)-ord('a'))
            
            sourceMask=0
            for c in word:
                sourceMask=wordMask^1<<(ord(c)-ord('a'))
                if sourceMask in s:
                    print(sourceMask, word)
                    count+=1
                    break
        return count