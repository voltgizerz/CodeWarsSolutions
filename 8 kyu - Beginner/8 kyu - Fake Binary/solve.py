def fake_bin(x):
    sum=""
    for i in x:
        if int(i)<5:
            sum+="0"
        else:
             sum+="1"
    return sum