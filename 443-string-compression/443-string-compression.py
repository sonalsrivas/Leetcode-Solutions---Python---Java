class Solution:
    def compress(self, chars: List[str]) -> int:
        compressedLen=0
        n=len(chars)
        i=0
        newIndex=0
        while i<n:
            count=0
            character=chars[i]
            ahead=i
            chars[newIndex]=chars[i]
            newIndex+=1
            while ahead<n and character == chars[ahead]:
                ahead+=1
                count+=1
            
            if count>1:
                for digit in str(count):
                    chars[newIndex]=digit; newIndex+=1
                compressedLen+=len(str(count))
            compressedLen+=1
            i=ahead
        
        return compressedLen