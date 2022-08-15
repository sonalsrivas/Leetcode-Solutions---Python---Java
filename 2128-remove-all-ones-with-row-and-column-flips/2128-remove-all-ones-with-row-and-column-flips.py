class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        pattern=grid[0]
        flippedPattern=[i^1 for i in pattern]
        for row in grid:
            if row!=pattern and row!=flippedPattern:
                return False
        return True
                    