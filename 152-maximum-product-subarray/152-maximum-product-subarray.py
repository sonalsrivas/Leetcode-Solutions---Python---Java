class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        prefixProduct=[x for x in nums]
        suffixProduct=[x for x in nums]
        for i in range(1,n):
            prefixProduct[i]*=prefixProduct[i-1] or 1
        for i in range(n-2, -1,-1):
            suffixProduct[i]*=suffixProduct[i+1] or 1
            #suffixProduct*=nums[i] or 1
        return max(max(prefixProduct), max(suffixProduct))
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)
        
'''

2 3 -2 4 0 -1 100 -100
       ^
                 ^
     -12
candidates =[6, (0,5)]
start from 0

*** move end p in the conditions: when end char>0 or (end char<0 and neg num count is even)

move my end pointer untill end char is a zero or neg nums count becomes odd

save the product untill now as a acandidate

if end char is a negative number and negnum count becomes odd, , lets include it
    then find the next neg num on right that would make prod positive again.
    
if do not find it uptill the end then,
    

'''