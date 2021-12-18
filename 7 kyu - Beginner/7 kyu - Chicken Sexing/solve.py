def correctness(bobs_decisions, expert_decisions):
    point = 0
    for i in range(0, len(bobs_decisions)):
        if bobs_decisions[i] ==  expert_decisions[i]:
            point += 1
        elif bobs_decisions[i] == "?" or expert_decisions[i] == "?":
            point += 0.5
    return point