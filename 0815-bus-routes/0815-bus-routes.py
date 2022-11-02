class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source== target:
            return 0
        adjacencyList=defaultdict(list)
        for bus, route in enumerate(routes):
            for busStation in route:
                adjacencyList[busStation].append(bus)
                
        mapBusRoutes={i:set(routes[i]) for i in range(len(routes))}
        q=deque()
        q.append((source,0))
        visitedStation = set([source])
        #q.append(None)
        #leastNumberOfBuses=0
        while q:
            station, noOfBuses = q.popleft()
            
            for possibleNextBus in adjacencyList[station]:
                for station in mapBusRoutes[possibleNextBus]:
                    if target in mapBusRoutes[possibleNextBus]:
                        return noOfBuses+1
                
                    q.append((station, noOfBuses+1))
                mapBusRoutes[possibleNextBus]=set()
        return -1