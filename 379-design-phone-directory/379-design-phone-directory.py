class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.pd=set()
        self.freeSlots=set([i for i in range(maxNumbers)])

    def get(self) -> int:
        if self.freeSlots:
            n=self.freeSlots.pop()
        else:
            return -1
        self.pd.add(n)
        return n

    def check(self, number: int) -> bool:
        if number in self.pd:
            return False
        return True

    def release(self, number: int) -> None:
        self.pd.discard(number)
        self.freeSlots.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)