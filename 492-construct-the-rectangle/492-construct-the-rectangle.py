class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area**0.5), 0,-1):
            if area%i==0:
                return sorted([i,area//i],reverse=True)
            
        
'''

find two closest numbers that prod to area

Approach:
1. Take the square root of the number (area)
2. from this new number upto 0 decrementing, 
3. return the first number that divides the area and the divisor


'''