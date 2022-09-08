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
                    #if numberOfDots>3:
                    #    return False
                    num=convertStrToNum(numStr)
                    if num is None or not 0<=num<=255 or numberOfDots>3:
                        return False
                    numStr=''
                elif not i.isdigit():
                    return False
                else:
                    numStr+=i
            num=convertStrToNum(numStr)
            #if num is None or not 0<=num<=255:
            #    return False
            return numberOfDots==3 and num and 0<=num<=255
        
        def validateIPv6(ip):
            numStr=''
            numberOfColons=0
            for i in ip:
                if i==':':
                    #if not numStr:
                    #    return False
                    numberOfColons+=1
                    if numberOfColons>7 or not numStr:
                        return False
                    numStr=''
                elif i.isdigit() or i in "abcdefABCDEF":
                    numStr+=i
                else:
                    return False
                if len(numStr)>4:
                    return False
            return numberOfColons==7 and numStr
        
        
        for i in queryIP:
            if i=='.':
                return "IPv4" if validateIPv4(queryIP) else "Neither"
            if i==':':
                return "IPv6" if validateIPv6(queryIP) else "Neither"
        return "Neither"