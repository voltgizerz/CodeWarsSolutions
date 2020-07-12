def decodeMorse(morse_code):
    morse_code = (morse_code.replace("   "," ..... ")).split()
    for i in range(len(morse_code)):
        morse_code[i] = MORSE_CODE[morse_code[i]]
    return ((''.join(morse_code)).replace("5"," ")).strip()