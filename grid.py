from unit.unit import Unit


class Grid():
    def __init__(self, size, unit_size):
        self.size = size
        self.unit_size = unit_size
        self.grid_size = int(self.size / self.unit_size)
        self.grid = [[Unit() for i in range(0, self.grid_size)] for j in range(0, self.grid_size)]

    def getUnitAtGrid(self, x, y):  # y before x
        return self.grid[y][x]

    def setUnitAtGrid(self, x, y, target):
        self.grid[y][x] = target

    def getGridSize(self):
        return self.grid_size

