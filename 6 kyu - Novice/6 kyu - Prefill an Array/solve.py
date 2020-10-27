def prefill(n=None,v=None):
    try:
        return [v for x in range(int(n))]
    except:
        return str(n)+" is invalid"