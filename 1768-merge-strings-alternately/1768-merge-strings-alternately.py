class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1, pointer2=0,0
        len1, len2=len(word1), len(word2)
        resultString=''
        while pointer1+pointer2<len1+len2:
            if pointer1<len1:
                resultString+=word1[pointer1]
                pointer1+=1
            if pointer2<len2:
                resultString+=word2[pointer2]
                pointer2+=1
        return resultString