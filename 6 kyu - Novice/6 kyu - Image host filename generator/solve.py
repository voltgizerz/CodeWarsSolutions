import random
import string
def generateName():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(6))