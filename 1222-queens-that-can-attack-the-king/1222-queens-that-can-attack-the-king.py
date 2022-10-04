'''
Chess board: 8*8
  Multiple Queens
  one King
  How many 
  
  queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
  
  
  Can I move the queen from is initial position to someother from where I can then attack th eking.
  
  
  * * *
  *
  @   
  
  queenCOl[0]=[0,1]
  
  A Queen has a valid move as:
   it can move diagonally
   move horizontally
   move vertically
   
 
 Approach:
 
  1. Start with the king
                             
  2. Look upwards vertically ^, untill a queen is found
  
  3. Look dow v , 
  4. 
  
  
  *
  *
  *       *
    *   
      @
    
  *
  *
  *
  
  
  0,0 0,1 0,2
  1,0 1,1 1,2
  2,0 2,1 2,2
  
  for the diagonal left-UP to right-DOWN.... to identify them by the exact difference
  and for other one.... by exact sum
  

https://leetcode.com/problems/queens-that-can-attack-the-king/
'''
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        n=8
        
        queensSet=set()
        for i,j in queens:
            queensSet.add((i,j))
        
        queensThatCanAttackList=[]
        
        i,j=king
        # upwards max value of i 
        for new_i in range(i-1, -1,-1):
            if (new_i,j) in queensSet:
                queensThatCanAttackList.append([new_i, j])
                break

        
        # and downwards min value of i
        for new_i in range(i+1, n):
            if (new_i, j) in queensSet:
                queensThatCanAttackList.append([new_i, j])
                break
        
        # left j
        for new_j in range(j-1, -1, -1):
            if (i, new_j) in queensSet:
                queensThatCanAttackList.append([i, new_j])
                break

        
        # right j
        for new_j in range(j+1, n):
            if (i, new_j) in queensSet:
                queensThatCanAttackList.append([i, new_j])
                break
        
        # diagonal upLeft starting from king
        diagonal_difference = i-j
        new_i, new_j=i-1, j-1
        while -1<new_i<n and  -1<new_j<n:
            if (new_i, new_j) in queensSet:
                queensThatCanAttackList.append([new_i, new_j])
                break
            new_i-=1
            new_j-=1
        
        # diagonal downRight starting from king
        new_i, new_j=i+1, j+1
        while -1<new_i<n and  -1<new_j<n:
            if (new_i, new_j) in queensSet:
                queensThatCanAttackList.append([new_i, new_j])
                break
            new_i+=1
            new_j+=1
            
        
        # diagonal upRight starting from king
        diagonal_sum = i+j
        new_i, new_j=i-1, j+1
        while -1<new_i<n and  -1<new_j<n:
            if (new_i, new_j) in queensSet:
                queensThatCanAttackList.append([new_i, new_j])
                break
            new_i-=1
            new_j+=1
        
        # diagonal downLeft starting from king
        new_i, new_j=i+1, j-1
        while -1<new_i<n and  -1<new_j<n:
            if (new_i, new_j) in queensSet:
                queensThatCanAttackList.append([new_i, new_j])
                break
            new_i+=1
            new_j-=1
        
        return queensThatCanAttackList
           
      
      