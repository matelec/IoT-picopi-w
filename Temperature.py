
def readTemp(I2C):
    buf = bytearray(1)  # création d’un buffer 1 octet
    buf[0] = 0x00  # adresse du registre point
    I2C.writeto(0x48, buf)  # écriture dans le LM75
    mesure = I2C.readfrom(0x48, 2)  # lecture 
    print("temperature en bin:", bin(mesure[0]), bin(mesure[1]))
    val = (mesure[0] << 3)|(mesure[1] >> 5) #reduction de 16 à 11bits.
    print(val)
    if (val > 1023):
        res =  (val ^ 0b11111111111)+1
        temperature = - res * 0.125
    else :
        temperature = val * 0.125
    print("temperature:",temperature)
    return temperature