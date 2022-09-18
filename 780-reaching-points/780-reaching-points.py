class Solution:
    def reachingPoints(self, a: int, b: int, x: int, y: int) -> bool:
        while x>a and y>b:
            x,y=x%y , y%x
        return (x==a and y>=b and (y-b)%a==0) or (y==b and x>=a and (x-a)%b==0)