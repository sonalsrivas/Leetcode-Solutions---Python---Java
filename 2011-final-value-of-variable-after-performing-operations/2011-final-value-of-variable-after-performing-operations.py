class Solution:
    def finalValueAfterOperations(self, o: List[str]) -> int:
        x=0
        for i in o:
            if i[1]=='-':
                x-=1
            else:
                x+=1
        return x