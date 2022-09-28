class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        mapChildrenCandies=[1]*n
        
        for i in range(1,n):
            currentRating = ratings[i]
            ratingToMyLeft = ratings[i-1]
            
            if currentRating > ratingToMyLeft:
                mapChildrenCandies[i] += mapChildrenCandies[i-1]
        
        for i in range(n-2, -1, -1):
            currentRating = ratings[i]
            ratingToMyRight = ratings[i+1]
            
            if currentRating > ratingToMyRight and mapChildrenCandies[i] <= mapChildrenCandies[i+1]:
                mapChildrenCandies[i] = mapChildrenCandies[i+1] +1
        
        return sum(mapChildrenCandies)