from unit.unit import Unit


class Grid():
    """Grid class for storing units

    :param size: Taille de la grille
    :type size: int
    :param unit_size: Taille de l'unité
    :type unit_size: int

    """
    def __init__(self, size, unit_size):
        """
        init function
        init the actual grid 

        
        """
        self.size = size
        self.unit_size = unit_size
        self.grid_size = int(self.size / self.unit_size)
        self.grid = [[0 for i in range(0, self.grid_size)] for j in range(0, self.grid_size)]

    def getUnitAtGrid(self, x, y):  # 
        """Recupère l'unité dans la grille

        :param x: Position de la case en x
        :type x: int
        :param y: Postion de la case en y
        :type y: int 
        :return: Donne l'unité présente à la case
        :rtype: Unit object

        """
        # y before x getter
        return self.grid[y][x]

    def setUnitAtGrid(self, x, y, target):  # 
        """Place une unité dans la grille
        
        :param x: Position de la case en x
        :type x: int
        :param y: Position de la case en y
        :type y: int
        :param target: Unité à placer
        :type target: Unit object

        """
        self.grid[y][x] = target
        target.pos_x = x
        target.pos_y = y

    def getGridSize(self): #
        """
        Donne la taille de la grille

        :return: Donne la taille de la grille
        :rtype: int

        """
        return self.grid_size

    def deleteUnitAtGrid(self, x, y): 
        """Supprime l'unité de la grille

        :param x: Position de la case en x
        :type x: int
        :param y: Position de la case en y
        :type y: int
        :return: Retourne la liste contenant les unités

        """
        self.grid[y][x] = 0
        return self.grid

    def moveUnitAtGrid(self, x, y, target):  # 
        """Deplace l'unité
        
        :param x: Position de la case en x
        :type: int
        :param y: Position de la case en y
        :type: int
        :param target: Unité à deplacer

        """
        self.deleteUnitAtGrid(target.getPosX(), target.getPosY())
        self.setUnitAtGrid(x, y, target)
