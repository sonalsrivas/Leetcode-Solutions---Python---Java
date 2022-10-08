class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        def checkIfHalfsSameTarget(target,lengthOfTarget):
            return lengthOfTarget%2==0 and target[:lengthOfTarget//2]==target[lengthOfTarget//2:]
        
        setOfSuffix=defaultdict(int) # length of the suffix string, number of occurrences of it
        setOfPrefix=defaultdict(int) # length of the prefix string, number of its occurences.
        
        for string in nums:
            length=len(string)
            if target.startswith(string):
                setOfPrefix[length]+=1
            if target.endswith(string):
                setOfSuffix[length]+=1
        
        lengthOfTarget=len(target)
        noOfPairs=0
        flagCheckTarget=checkIfHalfsSameTarget(target,lengthOfTarget)
        
        for suffix in setOfSuffix:
            if lengthOfTarget-suffix in setOfPrefix:
                if flagCheckTarget and suffix==lengthOfTarget-suffix:
                    noOfPairs+=(setOfSuffix[suffix]-1)*(setOfPrefix[lengthOfTarget-suffix])
                else:
                    noOfPairs+=setOfSuffix[suffix]*setOfPrefix[lengthOfTarget-suffix]
               
        return noOfPairs