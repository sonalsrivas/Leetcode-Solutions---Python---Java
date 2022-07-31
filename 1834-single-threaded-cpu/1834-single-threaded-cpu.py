import heapq


class Solution:
    def getOrder(self, tasks):
        n = len(tasks)
        orderOfTasks = []

        # Tasks Queue Pool
        TQ = []
        heapq.heapify(TQ)

        # Tasks Pool
        TP = [(tasks[i][0], i) for i in range(n)]
        heapq.heapify(TP)

        cpuBusyUntilTime = TP[0][0]
        # Untill not all tasks are known to be processed
        while TP or TQ:
            # add tasks to queue which are becoming available during cpu busy time
            while TP and TP[0][0] <= cpuBusyUntilTime:
                enqueTime, taskIndex = heapq.heappop(TP)
                heapq.heappush(TQ, (tasks[taskIndex][1], taskIndex))

            # choose to process a task
            if TQ:
                processingTime, taskProcessedIndex = heapq.heappop(TQ)
                orderOfTasks.append(taskProcessedIndex)
                cpuBusyUntilTime = cpuBusyUntilTime + processingTime

            else:
                cpuBusyUntilTime = TP[0][0]

        return orderOfTasks
