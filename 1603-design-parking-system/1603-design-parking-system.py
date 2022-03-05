class ParkingSystem:

    def __init__(self, b: int, m: int, s: int):
        self.t={1:b,2:m,3:s}

    def addCar(self, carType: int) -> bool:
        for type_ in self.t:
            if carType==type_:
                if self.t[type_]>0:
                    self.t[type_]-=1
                    return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)