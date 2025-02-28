
class LectureTemperature:
    def __init__(self, i2c):
          self.i2c = i2c
          self.temperature = None

    def readTemp(self):
        buf = bytearray(1)  # création d’un buffer 1 octet
        buf[0] = 0x00  # adresse du registre point
        self.i2c.writeto(0x48, buf)  # écriture dans le LM75
        mesure = self.i2c.readfrom(0x48, 2)  # lecture 
        val = (mesure[0] << 3)|(mesure[1] >> 5) #reduction de 16 à 11bits.
        if (val > 1023):                        #si valeur négative
            res =  (val ^ 0b11111111111)+1
            self.temperature = - res * 0.125
        else :                                  #si valeur positive              
            self.temperature = val * 0.125
        print("temperature:",self.temperature)
        return self.temperature