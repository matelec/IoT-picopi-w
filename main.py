from ConnectWifi import connect
import parametres
from Temperature import readTemp
from Affichage import oledTemp
from Envoyer import startMQTT
from machine import Pin, SoftI2C
import ssd1306
import time   

i2c = SoftI2C(scl=Pin(21), sda=Pin(20), freq=10000)
Oled_width = 128
Oled_height = 64
Oled = ssd1306.SSD1306_I2C(Oled_width, Oled_height, i2c)
buttonPin = Pin(19, Pin.IN)
temp=25

# définition de la fonction interruption bouton
def interrupt_button(pin):
    global temp
    oledTemp(Oled,temp)

buttonPin.irq(trigger=Pin.IRQ_RISING, handler=interrupt_button)

# définition du programme principal
def main():
    global temp
    ####appel de la fonction connection au wifi#####
    ssid = parametres.SSID
    password = parametres.PASSWORD
    #appel de la librairie ConnectWifi.
    print("Connexion au réseau Wi-Fi...")
    wlan = connect(ssid, password)
    #retour de la librairie.
    if wlan.isconnected():
        print("Connecté avec succès!")
        print("Adresse IP: ", wlan.ifconfig())
    else:
        print("Échec de la connexion.")

    while True:
        temp= readTemp(i2c)
        print (temp)
        startMQTT(temp)
        time.sleep(5)      

# programme principal.
if __name__ == "__main__":
    main()