def remove_unit(grid, id):
    for i in range(0, grid.getGridSize()):
        for j in range(0, grid.getGridSize()):

            unit = grid.getUnitAtGrid(i, j)
            if(unit != 0):
                if(unit.id == id):
                    grid.deleteUnitAtGrid(i, j)

