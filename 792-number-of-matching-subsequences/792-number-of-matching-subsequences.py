class Solution:
    def numMatchingSubseq(self, string: str, words: List[str]) -> int:
        bucketMap=defaultdict(list)
        
        # O n
        for word in words:
            bucketMap[word[0]].append(word)
            # assuming that words list has no duplicate words
            
        count=0
        for c in string:
            temp_map_c_=list()
            for word in bucketMap[c]:
                nextWord=word[1:]
                if nextWord=='':
                    count+=1
                    continue
                if nextWord[0]==c:
                    temp_map_c_.append(nextWord)
                else:
                    bucketMap[nextWord[0]].append(nextWord)
            bucketMap[c]=temp_map_c_
        return count
                