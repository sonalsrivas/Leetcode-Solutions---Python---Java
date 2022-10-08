class Solution:
    def compress(self, chars: List[str]) -> int:
        putPointer=0
        consecutiveStart=0
        consecutiveEnd=0
        n=len(chars)
        while consecutiveStart<n:
            character=chars[consecutiveStart]
            
            consecutiveEnd=consecutiveStart+1
            while consecutiveEnd<n and chars[consecutiveEnd]==character:
                consecutiveEnd+=1
            consecutiveLength=consecutiveEnd-consecutiveStart
            
            chars[putPointer]=character
            putPointer+=1
                
            if consecutiveLength>1:
                for digit in str(consecutiveLength):
                    chars[putPointer]=digit
                    putPointer+=1
            
            consecutiveStart=consecutiveEnd
        return putPointer