# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stackElem=[[nestedList,0,len(nestedList)]]
    
    def reachInteger(self):
        while self.stackElem:
            curElement, curIndex, curSize = self.stackElem[-1]
            if curIndex==curSize:
                self.stackElem.pop()
                continue
            if curElement[curIndex].isInteger():
                break
            newList=curElement[curIndex].getList()
            self.stackElem[-1][1]+=1
            self.stackElem.append([newList, 0, len(newList)])
            
    def next(self) -> int:
        self.reachInteger()
        curElement, curIndex, curSize = self.stackElem[-1]
        self.stackElem[-1][1]+=1
        return curElement[curIndex].getInteger()
    
    def hasNext(self) -> bool:
        self.reachInteger()
        return self.stackElem!=[]

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())