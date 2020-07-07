def validPhoneNumber(phoneNumber):
    return True if phoneNumber[0]=="(" and phoneNumber[4]==")" and phoneNumber[5]==" " and phoneNumber[9]=="-" and len(phoneNumber)==14 else False
