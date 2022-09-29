class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        
    #def findLongestConsecutiveWithKReplacement(string, k):
        start, end= 0,0
        n=len(string)
        mapCharFrequency = defaultdict(int)
        longestConsecutiveWithKReplacement = 0
        mapCharFrequency[string[end]] += 1
        
        while start<=end<n:
            #mapCharFrequency[string[end]] += 1
            maxFrequency=max(mapCharFrequency.values())
            #print("(end-start+1)-maxFrequency <= k   ",(end-start+1)- maxFrequency, k)
            if (end-start+1)-maxFrequency <= k:
                end+=1
                if end<n:
                    mapCharFrequency[string[end]] += 1
            else:
                mapCharFrequency[string[start]]-=1
                start+=1
            if end-start+1 > longestConsecutiveWithKReplacement:
                longestConsecutiveWithKReplacement = end-start+1
        
        return longestConsecutiveWithKReplacement-1