class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        setOfElements=set()
        for i in arr:
            if i*2 in setOfElements or (i%2==0 and i//2 in setOfElements):
                return True    
            else:
                setOfElements.add(i)
        return False
            
'''
1. put all elements in a set
2. or do this one by one
3. see if current element//2 or current*2 exists in the set
4. if it does, return True
'''