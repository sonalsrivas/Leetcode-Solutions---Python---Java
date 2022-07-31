class Solution:
    def equalPairs(self, a: List[List[int]]) -> int:
        storeRowWiseHash=collections.Counter()
        for row in a:
            element=''
            for col in row:
                element+=str(col)+','
            storeRowWiseHash[element]+=1
        n=len(a)
        count=0
        for j in range(n):
            element=''
            for i in range(n):
                element+=str(a[i][j])+','
            if element in storeRowWiseHash:
                count+=storeRowWiseHash[element]
        return count