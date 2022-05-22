def remove_unit(grid, id):
    for i in range(0, grid.getGridSize()):
        for j in range(0, grid.getGridSize()):
            unit = grid.getUnitAtGrid(i, j) #scan for the right unit to delete
            if(unit != 0): # unit different than nothing on grid
                if(unit.id == int(id)): 
                    grid.deleteUnitAtGrid(i, j)#it's the right unit
                    print("deleted unit")
                    return

def move_unit(grid, id, movement):
    for i in range(0, grid.getGridSize()):
        for j in range(0, grid.getGridSize()):
            unit = grid.getUnitAtGrid(i, j)
            if(unit != 0): 
                if(unit.id == int(id)): #scan for the right unit
                    grid.moveUnitAtGrid(unit.getPosX()+movement*unit.getAllegiance(), unit.getPosY(), unit)
                    print("moved unit")#it's the right unit
                    return
def animate_unit(grid, id):
    for i in range(0, grid.getGridSize()):
        for j in range(0, grid.getGridSize()):
            unit = grid.getUnitAtGrid(i, j)
            if(unit != 0): 
                if(unit.id == int(id)): #scan for the right unit
                    unit.changeSprite(2*unit.getAllegiance())
