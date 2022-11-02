class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source== target:
            return 0
        mapStationToBuses=defaultdict(list)
        for bus, route in enumerate(routes):
            for busStation in route:
                mapStationToBuses[busStation].append(bus)
                
        mapBusRoutes={i:set(routes[i]) for i in range(len(routes))}
        q=deque()
        q.append((source,0))
        #visitedStation = set([source])
        while q:
            station, noOfBuses = q.popleft()
            
            for possibleNextBus in mapStationToBuses[station]:
                for station in mapBusRoutes[possibleNextBus]:
                    if target in mapBusRoutes[possibleNextBus]:
                        return noOfBuses+1
                    #if station not in visitedStation:
                    q.append((station, noOfBuses+1))
                    #visitedStation.add(station)
                mapBusRoutes[possibleNextBus]=set()
        return -1