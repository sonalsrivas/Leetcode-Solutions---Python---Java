class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        #def is_match(text, pattern):
        text_n=len(text)
        pattern_n =len(pattern)
        dp = [[0 for i in range(text_n+1)]for j in range(pattern_n+1)]
        dp[0][0]=1

        i=1
        while i<pattern_n and pattern[i]=='*':
            dp[i+1][0]=1
            i+=2

        for pattern_i in range(pattern_n):
            for text_j in range(text_n):

                i,j = pattern_i+1, text_j+1

                if pattern[pattern_i] == text[text_j] or pattern[pattern_i]=='.':

                    dp[i][j] = dp[i-1][j-1]

                elif pattern[pattern_i] != text[text_j] and pattern[pattern_i] not in '.*':

                    dp[i][j] = 0

                elif pattern[pattern_i]=='*':

                    # no match
                    if not dp[i][j-1] or (pattern[pattern_i-1] != text[text_j] and pattern[pattern_i-1] !='.'):

                        dp[i][j] = dp[i-2][j]

                    else:

                        dp[i][j] = dp[i][j-1]
        #for row in dp:
        #    print(row)
        return dp[-1][-1]