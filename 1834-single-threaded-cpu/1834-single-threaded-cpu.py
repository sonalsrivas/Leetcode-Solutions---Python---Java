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

        cpuBusyUntillTime = TP[0][0]
        # Untill not all tasks are known to be processed
        while TP or TQ:
            # if TP:
            #     cpuBusyUntillTime = TP[0][0]
            # add tasks to queue which are becoming available during cpu busy time
            while TP and TP[0][0] <= cpuBusyUntillTime:
                enqueTime, taskIndex = heapq.heappop(TP)
                heapq.heappush(TQ, (tasks[taskIndex][1], taskIndex))

            # choose to process a task
            if TQ:
                processingTime, taskProcessedIndex = heapq.heappop(TQ)
                orderOfTasks.append(taskProcessedIndex)
                cpuBusyUntillTime = cpuBusyUntillTime + processingTime

            else:
                cpuBusyUntillTime = TP[0][0]
                #cpuBusyUntillTime += 1

        return orderOfTasks
