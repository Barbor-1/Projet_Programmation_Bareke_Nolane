from unit.unit import Unit


class Grid():
    def __init__(self, size, unit_size):
        """
        :param size: Taille de la grille
        :param unit_size: Taille de l'unité
        """
        self.size = size
        self.unit_size = unit_size
        self.grid_size = int(self.size / self.unit_size)
        self.grid = [[0 for i in range(0, self.grid_size)] for j in range(0, self.grid_size)]

    def getUnitAtGrid(self, x, y):  # Recupère l'unité dans la grille
        """
        :param x: Position de la case en x
        :param y: Postion de la case en y
        :return: Donne l'unité présente à la case
        """
        # y before x getter
        return self.grid[y][x]

    def setUnitAtGrid(self, x, y, target):  # Place une unité dans la grille
        """
        :param x: Position de la case en x
        :param y: Position de la case en y
        :param target: Unité à placer
        :return:
        """
        self.grid[y][x] = target
        target.pos_x = x
        target.pos_y = y

    def getGridSize(self): # Donne la taille de la grille
        """
        :return: Donne la taille de la grille
        """
        return self.grid_size

    def deleteUnitAtGrid(self, x, y): # Supprime l'unité de la grille
        """
        :param x: Position de la case en x
        :param y: Position de la case en y
        :return: Retourne la liste contenant les unités
        """
        self.grid[y][x] = 0
        return self.grid

    def moveUnitAtGrid(self, x, y, target):  # Deplace l'unité
        """
        :param x: Position de la case en x
        :param y: Position de la case en y
        :param target: Unité à deplacer
        :return:
        """
        self.deleteUnitAtGrid(target.getPosX(), target.getPosY())
        self.setUnitAtGrid(x, y, target)
