class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        countOfTeams=0
        for i in range(n):
            noOfSmallerOnLeft=0
            noOfGreaterOnLeft=0
            noOfSmallerOnRight=0
            noOfGreaterOnRight=0
            for left in range(0,i,1):
                if rating[left]>rating[i]:
                    noOfGreaterOnLeft+=1
                elif rating[left]<rating[i]:
                    noOfSmallerOnLeft+=1
            for right in range(i+1,n,1):
                if rating[right]>rating[i]:
                    noOfGreaterOnRight+=1
                elif rating[right]<rating[i]:
                    noOfSmallerOnRight+=1
            countOfTeams+=noOfSmallerOnLeft*noOfGreaterOnRight+noOfGreaterOnLeft*noOfSmallerOnRight
        return countOfTeams
'''

[2,5,3,4,1]
 0 1 2 3 4
 
 1 2 3 4 5
 4 0 2 3 1
 
 3
 2
 0
'''