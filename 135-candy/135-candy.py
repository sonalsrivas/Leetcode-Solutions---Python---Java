class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        mapChildrenCandies=[1]*n
        #minimumNoOfCandiesNeeded is atleast going to be as many children trhere are
  
        #mayeb initialize with ... minimumNoOfCandiesNeeded = len(ratings)
        for i in range(1,n):
            #i loops from 1 to the right end
            currentRating = ratings[i]
            ratingToMyLeft = ratings[i-1]
            
            if currentRating > ratingToMyLeft:
                mapChildrenCandies[i] += mapChildrenCandies[i-1]
        #print(mapChildrenCandies)
        for i in range(n-2, -1, -1):
            #i loops from n-2 to 0
            currentRating = ratings[i]
            ratingToMyRight = ratings[i+1]
            
            if currentRating > ratingToMyRight and mapChildrenCandies[i] <= mapChildrenCandies[i+1]:
                mapChildrenCandies[i] = mapChildrenCandies[i+1] +1
        #print(mapChildrenCandies)
        return sum(mapChildrenCandies)