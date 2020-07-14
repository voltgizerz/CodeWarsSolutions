def tower_builder(n_floors):
    list = []
    width = (n_floors * 2) - 1
    for i in range(1,n_floors+n_floors,2):
        list.append((i * '*').center(width))
    return  list