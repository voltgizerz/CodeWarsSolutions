def number(bus_stops):
    user = 0
    for x in range(len(bus_stops)):
        user+=bus_stops[x][0]-bus_stops[x][1]
    return user