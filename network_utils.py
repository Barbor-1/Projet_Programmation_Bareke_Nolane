import game
def remove_unit(grid, id):
    for i in range(0, grid.getGridSize()):
        for j in range(0, grid.getGridSize()):
            unit = grid.getUnitAtGrid(i, j)
            if(unit != 0):
                if(unit.id == int(id)):
                    grid.deleteUnitAtGrid(i, j)
                    print("deleted unit")

def move_unit(grid, id, inputQueue):
    for i in range(0, grid.getGridSize()):
        for j in range(0, grid.getGridSize()):
            unit = grid.getUnitAtGrid(i, j)
            if(unit != 0):
                if(unit.id == int(id)):
                    game.moveUnit(unit, grid, inputQueue, overrideRemove=True) # we now that this unit is a remote, we need to move it
                    print("moved unit")
