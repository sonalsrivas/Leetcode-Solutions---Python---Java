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
           
      
      