# return the minimum required waterbombs to extinguish the fires in the array
def waterbombs(fire, w):
    cnt = 0
    limit = w
    for i in range(len(fire)):
        if fire[0] == 'Y':
            pass
        elif fire[i] == 'Y' and w == 1:
            pass
        elif fire[i] == 'Y':
            cnt += 1
        else:
            if limit == 0:
                cnt += 1
                limit = w
            else:
                print("masok")
                if w == 1:
                    cnt += 1
                limit -= 1
                if i == len(fire)-1:
                    cnt +=1
    print(fire, w, cnt)
    return cnt


print(waterbombs("xxxxxYxYx", 2))
