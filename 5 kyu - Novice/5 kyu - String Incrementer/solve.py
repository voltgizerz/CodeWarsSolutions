import re
def increment_string(strng):
    if re.match('.*?([0-9]+)$', strng) == None:
        last_digits = strng+"1"
    else:
        last_digits = re.match('.*?([0-9]+)$', strng).group(1)
        last_digits = strng[0:len(strng)-len(last_digits)]+(str(int(last_digits)+1)).zfill(len(last_digits))
    return last_digits