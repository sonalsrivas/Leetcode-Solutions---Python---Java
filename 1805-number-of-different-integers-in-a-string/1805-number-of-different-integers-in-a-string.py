class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        setOfNumbers=set()
        n=len(word)
        i=0
        while i<n:
            while i<n and not word[i].isdigit():
                i+=1
            num=''
            while i<n and word[i].isdigit():
                num+=word[i]
                i+=1
            if num:
                setOfNumbers.add(int(num))
            
        return len(setOfNumbers)