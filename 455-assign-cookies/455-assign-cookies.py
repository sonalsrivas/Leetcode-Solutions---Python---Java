class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gl=len(g)
        sl=len(s)
        g.sort()
        s.sort()
        i,j=0,0
        countOfHappyChildren=0
        
        while i < gl and j< sl:
            if s[j]>=g[i]:
                countOfHappyChildren+=1
                i+=1
                j+=1
            else:
                j+=1
        
        return countOfHappyChildren
                
'''
greed factor : mini size of cookie a child will be content with 

cookie size array

size[j]>=greed[i] child i happy!!!

maximize happy children.

g = [1,2,3], s = [1,1]

Approach:: 
1. sort the g and s arrays
2. place two pointers on each array and assign greedily as you go along.
3. and keep count of the same.


Failing Example: 
[10,9,8,7]
[5,6,7,8]

7,8,9,10
^
5 6 7 8
^
'''