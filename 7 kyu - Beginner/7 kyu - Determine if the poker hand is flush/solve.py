def is_flush(cards):
    start =cards[0]
    for i in cards:
        if i[-1] != start[-1]:
            return False
    return True