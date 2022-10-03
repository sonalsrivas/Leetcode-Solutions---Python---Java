class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n1=len(list1)
        d1={list1[i]:i for i in range(n1)}
        n2=len(list2)
        d2={list2[i]:i for i in range(n2)}
        minimumIndexSum=float('inf')
        minimumIndexSumWord=''
        for word in d1:
            if word in d2:
                d1[word]+=d2[word]
                minimumIndexSum=min(minimumIndexSum, d1[word])
            else:
                d1[word]=-1
        resultList=[]
        for word in d1:
            if d1[word]==minimumIndexSum:
                resultList.append(word)
        return resultList