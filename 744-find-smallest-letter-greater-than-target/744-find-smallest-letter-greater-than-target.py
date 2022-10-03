class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n=len(letters)
        left, right=0, n-1
        while left<=right:
            mid=(left+right)//2
            if target < letters[mid]:
                right=mid-1
            elif letters[mid] <= target :
                left=mid+1
            else:
                #print
                return letters[(mid+1)%n]
            
        return letters[(left)%n]
        
'''

binary search for the target character

'''