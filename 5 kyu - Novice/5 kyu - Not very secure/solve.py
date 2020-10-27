import re
def alphanumeric(password): 
    return True  if re.search("^[a-zA-Z0-9]*$",password) and password!="" else False