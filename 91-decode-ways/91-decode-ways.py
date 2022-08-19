import string
class Solution:
    def numDecodings(self, S: str) -> int:
        n=len(S)
        noOfUniqueWaysToDecode=[0]*n
      
        def noOfWaysToEncodeIthChar(i):
            if i>=n:
                return 1

            if noOfUniqueWaysToDecode[i]!=0:
                return noOfUniqueWaysToDecode[i]
            
            if S[i]=='0':
                return 0
            
            elif '0'<S[i]<'3':
                if i+1<n and S[i+1]=='0':
                    noOfUniqueWaysToDecode[i]=noOfWaysToEncodeIthChar(i+2)
                elif i+1<n and S[i]=='2' and S[i+1]>'6':
                    noOfUniqueWaysToDecode[i]=noOfWaysToEncodeIthChar(i+1)
                elif i+1<n and S[i+1]!='0':
                    noOfUniqueWaysToDecode[i] = noOfWaysToEncodeIthChar(i+2) + noOfWaysToEncodeIthChar(i+1)
                elif i+1==n:
                    noOfUniqueWaysToDecode[i]+=1 
            else:
                if i+1<n and S[i+1]!='0':
                    noOfUniqueWaysToDecode[i]=noOfWaysToEncodeIthChar(i+1)
                elif i+1<n and S[i+1]=='0':
                    noOfUniqueWaysToDecode[i]=0
                else:
                    noOfUniqueWaysToDecode[i]+=1
            return noOfUniqueWaysToDecode[i]

        return noOfWaysToEncodeIthChar(0)