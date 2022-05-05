import unit.unit


class grid():
    def __init__(self, size, unit_size):
        self.size = size
        self.unit_size = unit_size
        self.grid_size = self.size / self.unit_size
        self.grid = [[Unit() for i in range(0, self.grid_size)] for j in range(0, self.grid_size)]

    def getUnitAtGrid(self, x, y):  # y before x
        return self.grid[y][x]

    def setUnitAtGrid(self, x, y, unit):
        self.grid[y][x] = unit
