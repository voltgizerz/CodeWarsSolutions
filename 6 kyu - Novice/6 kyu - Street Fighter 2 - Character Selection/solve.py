def street_fighter_selection(fighters, initial_position, moves):
    rows = 0
    start = 0
    select = []
    for i in moves:
        if i =="up":
            rows =0
        elif i =="down":
            rows =1
        elif i =="right":
            start = (start+1)%(len(fighters[rows]))
        elif i =="left":
            start = (start-1)%(len(fighters[rows]))
        select.append(fighters[rows][start])
    return select