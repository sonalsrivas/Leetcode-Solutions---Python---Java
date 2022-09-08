class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def convertStrToNum(numStr):
            if not numStr:
                return
            num=0
            firstd=''
            for d in numStr:
                if firstd=='0':
                    return None      
                num*=10
                num+=ord(d)-ord('0')
                if not firstd:
                    firstd+=d
            return num
        def validateIPv4(ip):
            numStr=''
            numberOfDots=0
            for i in ip:
                if i=='.':
                    numberOfDots+=1
                    num=convertStrToNum(numStr)
                    if num is None or not 0<=num<=255 or numberOfDots>3:
                        return False
                    numStr=''
                elif not i.isdigit():
                    return False
                else:
                    numStr+=i
            num=convertStrToNum(numStr)
            return numberOfDots==3 and num and 0<=num<=255
        
        def validateIPv6(ip):
            numStr=0
            numberOfColons=0
            for i in ip:
                if i==':':
                    numberOfColons+=1
                    if numberOfColons>7 or numStr==0:
                        return False
                    numStr=0
                elif i.isdigit() or i in "abcdefABCDEF":
                    numStr+=1
                else:
                    return False
                if numStr>4:
                    return False
            return numberOfColons==7 and numStr>0
        
        
        for i in queryIP:
            if i=='.':
                return "IPv4" if validateIPv4(queryIP) else "Neither"
            elif i==':':
                return "IPv6" if validateIPv6(queryIP) else "Neither"
        return "Neither"