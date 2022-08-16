class Solution:
    def findTheWinner(self, numberOfFriends: int, k: int) -> int:
        winner=0
        for i in range(1,numberOfFriends+1):
            winner=(winner+k)%i
        return winner+1