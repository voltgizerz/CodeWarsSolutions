def find_outlier(integers):
    even = list(filter(lambda x: (x % 2 == 0), integers))
    odd = list(filter(lambda x: (x % 2 == 1), integers)) 
    return odd[0] if len(odd)==1 else even[0]