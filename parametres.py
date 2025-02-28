import ubinascii
import machine

#SSID= "AP-IOT-BPCIEL"
#PASSWORD= "wificielCIEL2024$"

SSID= "wifi627"
PASSWORD= "4ddi54?*ehhp3PJW"


MQTT_TOPIC= " ici le topic "

mqtt_server = "adresse IP de votre RPI ZERO 2W" # Remplacez par vos infos
# Création de l'identifiant
mqtt_client_id = ubinascii.hexlify(machine.unique_id())
usermqtt = "utilisateur enregistré sur le broker"
usermdp = "mot de passe de l'utilisateur"
