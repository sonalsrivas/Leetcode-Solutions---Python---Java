# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    allDirections=((0,-1),(-1,0),(0,1),(1,0))
    def cleanRoom(self, robot):
        
        visitednCleaned=set()
        def cleannBacktrack(x,y,direction):
            robot.clean()
            visitednCleaned.add((x,y))
            
            for i in range(4):
                direc=(direction+i)%4
                i,j=Solution.allDirections[direc]
                i+=x
                j+=y
                if (i,j) not in visitednCleaned and robot.move():
                    cleannBacktrack(i,j,direc)
                robot.turnRight()
                
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        cleannBacktrack(0,0,0)