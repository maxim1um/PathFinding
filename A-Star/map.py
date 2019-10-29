import numpy as np
from point import Point

class RandomMap:
    def __init__(self, size=50):
        self.size = size
        self.grid = []

    def SetupMap(self):
        self.InitMap()
        bResult = self.CreateCentralObstacles()
        if bResult == False:
            return False
        
        return True
        

    def InitMap(self):
        # Init the whole map with defualt value
        self.CreateMapGrid()
        # Crate the boundry
        self.CreateBoundry()
    
    def CreateMapGrid(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid.append(Point(i, j))

    def CreateBoundry(self):
        for point in self.grid:
            if point.x == 0 or point.x == self.size-1 or point.y == 0 or point.y == self.size-1:
                point.value = -2

    def CreateCentralObstacles(self, size=8):
        # Check the map size is bigger than obstacles
        if self.size//2-1 <= size//2:
            return False

        # The cetral obstacle size is 8*8
        obstacles = []
        for i in range(self.size//2-(size//2), self.size//2):
            obstacles.append(Point(i, self.size-i))
            obstacles.append(Point(i, self.size-i-1))
            obstacles.append(Point(self.size-i, i))
            obstacles.append(Point(self.size-i, i-1))
        obstacles.append(Point(self.size//2, self.size-self.size//2))
        obstacles.append(Point(self.size//2, self.size-self.size//2 -1))

        # Set obstacls value in to map grid
        for ob in obstacles:
            for grid in self.grid:
                if ob.x == grid.x and ob.y == grid.y:
                    grid.value = -1

        return True
         
