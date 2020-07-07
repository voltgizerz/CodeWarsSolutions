def count_smileys(arr):
    cnt =0
    for i in arr:
        if len(i)==2:
            if ((":" in i or ";" in i) and (")" in i or "D" in i)):
                cnt +=1
        else:
            if ((":" in i or ";" in i) and (")" in i or "D" in i) and ("~" in i or "-" in i)):
                cnt +=1     
    return cnt 