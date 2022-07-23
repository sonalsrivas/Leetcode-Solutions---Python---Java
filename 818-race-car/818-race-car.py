class Solution:
    def racecar(self, t: int) -> int:
        priorityQueue = [(0, 0, 1)]
        heapq.heapify(priorityQueue)
        visitedPositions = set()

        def bfsRaceCarPositionsSpeed(t):
            while priorityQueue:
                Top = heapq.heappop(priorityQueue)
                steps, position, speed = Top
                if position == t:
                    return steps
                if (position, speed) in visitedPositions:
                    continue
                else:
                    visitedPositions.add((position, speed))
                    if t >= speed >= -t:
                        heapq.heappush(priorityQueue, (steps + 1, position + speed, speed * 2))
                    if (position + speed > t and speed > 0) or (position + speed < t and speed < 0):
                        heapq.heappush(priorityQueue, (steps + 1, position, -1 if speed > 0 else 1))
            return -1

        return bfsRaceCarPositionsSpeed(t)