def naughty_or_nice(data):
    nau = 0
    nic = 0
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    for x in range(len(data)):
        for n,v in data[months[x]].items():
            if v=="Naughty":
               nau+=1
            else:
               nic+=1
    return "Nice!" if nic>nau or nic==nau else "Naughty!"