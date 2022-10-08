class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons=persons
        self.times = times
        self.n=len(self.times)
        self.leading=[0]*self.n
        self.populateLeading()

    def q(self, t: int) -> int:
        index=self.binarySearch(t)
        print(index,t)
        return self.leading[index]
    
    def binarySearch(self, time):
        # returns equal or prev smaller time ::
        left, right=0, self.n-1
        while left<right:
            mid=(left+right)//2
            #if self.times[mid]==time:
            #    return mid
            if self.times[mid]<=time:
                if mid+1>=self.n or self.times[mid+1]>time:
                    return mid
                left=mid+1
            else:
                right=mid-1
        return left
        
    def populateLeading(self):
        mapPersonVotes=defaultdict(int)
        leadingVotes=1
        self.leading[0]=self.persons[0]
        mapPersonVotes[self.persons[0]]+=1
        for i in range(1,self.n):
            mapPersonVotes[self.persons[i]]+=1
            if mapPersonVotes[self.persons[i]]>=mapPersonVotes[self.leading[i-1]]:
                self.leading[i]=self.persons[i]
            else:
                self.leading[i]=self.leading[i-1]
        print(self.leading)
        

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
'''
person = [0, 1, 0, 0, 0, 1, 0], 
                          ^
time = [0, 5, 10, 15, 20, 25, 30]
                          ^
ldVot= [1, 1, 2,  3,  4,  2,  5]
leadi=  0, 1, 0,  0,  0,  0,  0
        previous leading >=current person's vote  than change lead
0 1 1 0 0 1
15,1
5,1
0,0

'''