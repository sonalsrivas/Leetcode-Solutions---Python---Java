class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n==0:
            return str(n)
        reversedString=''
        noOfDigits=0
        while n>0:
            digit=n%10
            noOfDigits+=1
            if noOfDigits==4:
                reversedString+='.'
                noOfDigits=1
            reversedString+=chr(ord('0')+digit)
            
            n//=10
            
        return reversedString[::-1]
'''
for every third number, do sep
'''