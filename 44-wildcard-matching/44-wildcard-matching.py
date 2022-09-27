class Solution:
    def isMatch(self, string, pattern):
        string_n=len(string)
        pattern_n=len(pattern)
        dp=[[0 for i in range(string_n+1)] for j in range(pattern_n+1)]
        dp[0][0]=1
        i=0
        while i<pattern_n and pattern[i]=='*':
            dp[i+1][0]=1
            i+=1
        for pattern_j in range(1,pattern_n+1):
            for string_i in range(1,string_n+1):
                if pattern[pattern_j-1]=='?' or pattern[pattern_j-1]==string[string_i-1]:
                    dp[pattern_j][string_i]=dp[pattern_j-1][string_i-1]
                elif pattern[pattern_j-1]=='*':
                    dp[pattern_j][string_i]=dp[pattern_j-1][string_i-1] or dp[pattern_j][string_i-1]  or dp[pattern_j-1][string_i]
        for row in dp:
            print(row)
        return dp[-1][-1]
