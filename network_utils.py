def remove_unit(grid, id):
    for i in range(0, len(grid.getGridSize())):
        for j in range(0, len(grid.getGridSize())):

        unit = grid.getUnitAtGrid(i, j)
        if(unit != 0):
            if(unit.id == id):
                grid.deleteUnitAtGrid(i, j)
                print("new unit list", unit_list)
                return unit_list
        print("new unit list", unit_list)
        return unit_list

