import hashlib
def pass_hash(str):
    return hashlib.md5(str.encode()).hexdigest()