class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substringCharSet=set()
        start=0
        n=len(s)
        longestSubstringLength=min(1,n)
        for end in range(n):
            if s[end] in substringCharSet:
                longestSubstringLength=max(longestSubstringLength, end-start)
                while s[start]!=s[end]:
                    substringCharSet.remove(s[start])
                    start+=1
                start+=1
            else:
                longestSubstringLength=max(longestSubstringLength, end-start+1)
                substringCharSet.add(s[end])
        return longestSubstringLength