def binarySearch(a, target):
    left = 0
    right = len(a) - 1
    while left < right:
        middle = (left + right) // 2
        if a[middle][0] < target:
            left = middle + 1
        else:
            right = middle
    return left if a[left][
                       0] >= target else left + 1  # Edge Case ... when the answer index is at the rear ends of the array


class SnapshotArray:
    def __init__(self, length: int):
        self.snapID = -1
        self.record = [[[-1, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.record[index][-1][0] != self.snapID:
            self.record[index].append([self.snapID, val])
        else:
            self.record[index][-1][1] = val

    def snap(self) -> int:
        self.snapID += 1
        return self.snapID

    def get(self, index: int, snap_id: int) -> int:
        return self.record[index][binarySearch(self.record[index], snap_id) - 1][1]
