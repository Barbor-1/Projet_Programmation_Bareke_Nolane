def remove_unit(unit_list, id):
    for i in range(0, len(unit_list)):
        if (unit_list[i].id == id):
            unit_list.pop(i)
            print("new unit list", unit_list)
            return unit_list
        print("new unit list", unit_list)
        return unit_list

