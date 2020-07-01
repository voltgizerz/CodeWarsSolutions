def create_phone_number(n):
    phoneNumber = '('
    for i in range(len(n)):
        phoneNumber = phoneNumber + str(n[i])
    return phoneNumber[:4] + ') '+phoneNumber[4:7]+'-'+phoneNumber[7:]
