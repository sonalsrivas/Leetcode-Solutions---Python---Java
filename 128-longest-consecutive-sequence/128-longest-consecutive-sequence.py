class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNums=set(nums)
        longestConsecutiveSequence=0
        for element in nums:
            nextConsecutive=element
            while nextConsecutive in setOfNums:
                setOfNums.remove(nextConsecutive)
                nextConsecutive += 1
            longestConsecutiveSequence = max(longestConsecutiveSequence, nextConsecutive - element)

            if nextConsecutive > element:
                nextConsecutive -= 1
            prevConsecutive = element-1

            while prevConsecutive in setOfNums:
                setOfNums.remove(prevConsecutive)
                prevConsecutive -= 1
            longestConsecutiveSequence = max(longestConsecutiveSequence, nextConsecutive - prevConsecutive)
        return longestConsecutiveSequence