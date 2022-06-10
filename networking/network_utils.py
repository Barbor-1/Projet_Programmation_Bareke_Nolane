def remove_unit(grid, id):  
    """ remove unit for client

    :param grid: grid
    :type grid: Grid
    :param id: id of unit to remove
    :type id: int

    """
    for i in range(0, grid.getGridSize()):
        for j in range(0, grid.getGridSize()):
            unit = grid.getUnitAtGrid(i, j)  # scan for the right unit to delete
            if (unit != 0):  # unit different than nothing on grid
                if (unit.id == int(id)):  # scan for the right unit
                    grid.deleteUnitAtGrid(i, j)  # it's the right unit
                    print("deleted unit")
                    return


def move_unit(grid, id, movement):  #
    """move unit for client

    :param grid: grid
    :type grid: Grid
    :param id: id of unit to remove
    :type id: int
    :param movement: what to move for the said unit (int or float, if float (=1.5) it means that there is a tick to wait before moving the unit)
    :type movement:  float 
    """

    for i in range(0, grid.getGridSize()):
        for j in range(0, grid.getGridSize()):
            unit = grid.getUnitAtGrid(i, j)
            if (unit != 0):  # if grid is a unit (0 = empty)
                if (unit.id == int(id)):  # scan for the right unit
                    if (movement % 1 == 0.5):

                        movement -= 0.5  # so that movement = 1
                        print("unit is in water")
                        unit.changeSprite(3 * unit.getAllegiance())  # water sprite
                        new_pos_x = unit.getPosX() + 0.5 * unit.getAllegiance()  # new pos x with half movement in water

                        if (unit.half_walk == True):  # we can move, we were aleady stoped last time we moved
                            grid.moveUnitAtGrid(unit.getPosX() + 1 * unit.getAllegiance(), unit.getPosY(), unit)
                            unit.half_walk = False  # reset the flag
                        print("moved unit")  # it's the right unit
                        unit.half_walk = True

                    else:
                        unit.changeSprite(unit.getAllegiance())  # reset sprite
                        grid.moveUnitAtGrid(unit.getPosX() + int(movement) * unit.getAllegiance(), unit.getPosY(),
                                            unit)  # move unit
                        print("moved unit")  # it's the right unit
                    return


def animate_unit(grid, id):  # 
    """animate unit for client

    :param grid: grid
    :type grid: Grid
    :param id:  id of the unit to animate
    :type id: int
    """
    for i in range(0, grid.getGridSize()):
        for j in range(0, grid.getGridSize()):
            unit = grid.getUnitAtGrid(i, j)
            if (unit != 0):  # if grid is a unit (0 = empty)
                if (unit.id == int(id)):  # scan for the right unit
                    unit.changeSprite(
                        2 * unit.getAllegiance())  # *2 : on peut differencier l'allegiance en appelant avec 2*allegiance
