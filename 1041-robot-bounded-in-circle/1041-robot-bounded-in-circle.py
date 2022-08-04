class Robot:
    directions = 'ENWS'
    directionXY = {'E': [1, 0], 'N': [0, 1], 'W': [-1, 0], 'S': [0, -1]}
    indexDirection = {x: i for i, x in enumerate('ENWS')}

    def __init__(self):
        self.robotFacingDirection = 'E'
        self.robotPosition = [0, 0]
        
    def moveAhead(self):
        self.robotPosition[0] += Robot.directionXY[self.robotFacingDirection][0]
        self.robotPosition[1] += Robot.directionXY[self.robotFacingDirection][1]
        return self.robotPosition==[0,0]
            

    def changeDirectionClockwise(self):
        index = (Robot.indexDirection[self.robotFacingDirection] + 3) % 4
        self.robotFacingDirection = Robot.directions[index]

    def changeDirectionAntiClockwise(self):
        index = (Robot.indexDirection[self.robotFacingDirection] + 1) % 4
        self.robotFacingDirection = Robot.directions[index]


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        robot = Robot()
        for command in instructions:
            if command == 'G':
                isCurPosOrigin=robot.moveAhead()
            elif command == 'L':
                robot.changeDirectionAntiClockwise()
            else:
                robot.changeDirectionClockwise()
        return robot.robotPosition == [0, 0] or robot.robotFacingDirection!='E'