
class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector=nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, otherVector: 'SparseVector') -> int:
        n=len(otherVector.vector)
        dotProd=0
        #print(self.vector)
        for i in range(n):
            dotProd+=self.vector[i]*otherVector.vector[i]
        return dotProd

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)