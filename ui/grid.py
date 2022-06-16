from unit.unit import Unit


class Grid():
    """Grid class for storing units

    :param size: size of the grid
    :type size: int
    :param unit_size: size of the unit
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
        """get a unit at a position

        :param x: x coordinate of the unit
        :type x: int
        :param y: y coordinate of the unit
        :type y: int 
        :return: the unit at the (x,y) position
        :rtype: Unit object

        """
        # y before x getter
        return self.grid[y][x]

    def setUnitAtGrid(self, x, y, target):  # 
        """put a unit in the grid
        
        :param x: x coordinate of the case where the unit will be put
        :type x: int
        :param y: ycoordinate of the case where the unit will be put
        :type y: int
        :param target: unit to place
        :type target: Unit object

        """
        self.grid[y][x] = target
        target.pos_x = x
        target.pos_y = y

    def getGridSize(self): #
        """
        return the grid size(square)

        :return: the grid size
        :rtype: int

        """
        return self.grid_size

    def deleteUnitAtGrid(self, x, y): 
        """delete a unit from the grid

        :param x: x coordinate of the case where the unit will be deleted
        :type x: int
        :param y: y coordinate of the case where the unit will be put
        :type y: int
        :return: the grid modified

        """
        self.grid[y][x] = 0
        return self.grid

    def moveUnitAtGrid(self, x, y, target):  # 
        """move the unit
        
        :param x: x coordinate of the case where the unit is before being moved
        :type x: int
        :param y: y coordinate of the case where the unit is before being moved
        :type y: int
        :param target: Unit to move
        :type target: Unit object

        """
        self.deleteUnitAtGrid(target.getPosX(), target.getPosY())
        self.setUnitAtGrid(x, y, target)
