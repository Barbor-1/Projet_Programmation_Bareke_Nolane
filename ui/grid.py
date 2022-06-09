from unit.unit import Unit


class Grid():
    def __init__(self, size, unit_size):
        self.size = size
        self.unit_size = unit_size
        self.grid_size = int(self.size / self.unit_size)
        self.grid = [[0 for i in range(0, self.grid_size)] for j in range(0, self.grid_size)]

    def getUnitAtGrid(self, x, y):  # Recupère l'unité dans la grille
        # y before x getter
        return self.grid[y][x]

    def setUnitAtGrid(self, x, y, target):  # Place une unité dans la grille
        self.grid[y][x] = target
        target.pos_x = x
        target.pos_y = y

    def getGridSize(self): # Donne la taille de la grille
        return self.grid_size

    def deleteUnitAtGrid(self, x, y): # Supprime l'unité de la grille
        self.grid[y][x] = 0
        return self.grid

    def moveUnitAtGrid(self, x, y, target):  # Deplace l'unité
        self.deleteUnitAtGrid(target.getPosX(), target.getPosY())
        self.setUnitAtGrid(x, y, target)
