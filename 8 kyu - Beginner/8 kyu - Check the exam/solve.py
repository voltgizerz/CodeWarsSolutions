def check_exam(arr1,arr2):
    sum =0
    for i in range(len(arr1)):
        if arr2[i]==arr1[i]:
            sum+=4
        elif arr2[i]!=arr1[i] and arr2[i]!='':
            sum -=1    
    return 0 if sum<0 else sum