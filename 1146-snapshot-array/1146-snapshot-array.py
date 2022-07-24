def binarySearch(a, t):
    l=0
    r=len(a)-1
    while l<r:
        m=(l+r)//2
        if a[m][0]<t:
            l=m+1
        #elif a[m][0]==t:
        #    return m+1
        else:
            r=m
    #print(l)
    return l if a[l][0]>=t else l+1
class SnapshotArray:

    def __init__(self, length: int):
        self.snapID=-1
        self.record=[[[-1,0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.record[index][-1][0]!=self.snapID:
            self.record[index].append([self.snapID, val])
        else:
            self.record[index][-1][1]=val

    def snap(self) -> int:
        self.snapID+=1
        return self.snapID
        
    def get(self, index: int, snap_id: int) -> int:
        #print("self.record[index]=> ",self.record[index])
        return self.record[index][binarySearch(self.record[index], snap_id)-1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)