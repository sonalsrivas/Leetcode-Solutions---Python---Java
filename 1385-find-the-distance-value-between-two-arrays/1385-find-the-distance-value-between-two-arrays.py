class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        n=len(arr1)
        
        def binarySearch(target):
            left, right=0,n2
            while left< right:
                mid=(left+right)//2
                if arr2[mid]<target:
                    left=mid+1
                elif target< arr2[mid]:
                    right=mid
                else:
                    return mid
            return left
        
        count=0
        arr2.sort()
        #arr2.insert(0,-float('inf'))
        #arr2.append(float('inf'))
        print(arr2)
        n2=len(arr2)
        for a1 in arr1:
            index = binarySearch(a1)
            leftNumber=None
            rightNumber=None
            print(a1, index)
            if index>0:
                leftNumber=arr2[index-1]
                print(f"leftNumber={leftNumber}")
                if a1-d<=leftNumber:
                    continue
            if index<=n2-1:
                theNumber=arr2[index]
                print(f"theNumber={theNumber}")
                if a1+d>=theNumber:
                    continue
            if index<n2-1:
                rightNumber=arr2[index+1]
                print(f"rightNumber={rightNumber}")
                if a1+d>=rightNumber:
                    continue
            print("true for ",a1)
            count+=1
            
        return count
'''
1 8 9 10

a1+d=right
a1-d=left

if elements greater than left and right exists for an element then do not count it.
1. Sort the arr2
2. binary search for the left and right seperartely 
 ..... for equal or greater
3. 


'''