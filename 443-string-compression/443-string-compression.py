class Solution:
    def compress(self, chars: List[str]) -> int:
        compressedLen=0
        n=len(chars)
        i=0
        newIndex=0
        while i<n and newIndex<n:
            count=0
            chars[newIndex]=chars[i]
            while i<n and chars[i] == chars[newIndex]:
                i+=1
                count+=1
            newIndex+=1
            if count>1:
                strCount=str(count)
                for digit in strCount:
                    chars[newIndex]=digit; newIndex+=1
                compressedLen+=len(strCount)
            compressedLen+=1
        
        return compressedLen