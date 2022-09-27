class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        left, right= min(nums)-1,max(nums)+1
        trackerDict={i:0 for i in range(left, right)}  # thsi element is not visited
        for element in nums:
            trackerDict[element]+=1  # and 1 indicates that it is visited, or hat this num exists in teh nums array

        sumOfMinPairs=0
        numsEncountered=0
        for i in range(left, right):
             if trackerDict[i]==0:
                pass
             else:
                while trackerDict[i]>0:
                    numsEncountered+=1
                    if numsEncountered % 2==1:
                        sumOfMinPairs += i
                    trackerDict[i]-=1
        return sumOfMinPairs