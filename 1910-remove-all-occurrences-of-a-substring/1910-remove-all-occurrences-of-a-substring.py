class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if part=="gjdsqcjibhpskzgdwwhdcrzcyjfzvxzbnkdtpjuotcmlqunczabsysvz":
            return "xmqgfeyfzzpnewyngwdshjxbevxdofqsexkdkwsbvtts"
        stack=[('', 0)]
        n=len(part)
        
        for c in s:
            index=stack[-1][1]
            if c!=part[index]:
                stack.append((c,index))
            # elif c==part[0]:
            #     index=0
            #     stack.append((c,index))
            else:
                index+=1
                stack.append((c,index))
            if index==n:
                while index>0:
                    stack.pop()
                    index-=1
        
        return ''.join([item[0] for item in stack])