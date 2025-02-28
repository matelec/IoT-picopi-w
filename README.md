# IoT-picopi-w
---
## Projet IoT BP CIEL 
---
Voici le dépot du firmware des IoTs à base de Raspberry Pico Pi W. Le firmware est codé à la suite du module 6: IoT. 

* `lib`: contient les librairies ssd1306 pour contrôler les écrans Oled et umqtt_simple pour communiquer avec le protocole MQTT.
* 
---

Les paramètres sensibles sont enregistrés dans un fichier config.json. Vous devez respecter la structure suivante:
- {
- "wifi_ssid": "le ssid",
- "wifi_password": "la clé",
    - "mqtt_broker": "l'adresse IP",
    - "mqtt_topic": "le topic",
    - "mqtt_user": "le compte user",
    - "mqtt_password": "mon_mdp"
    -    }
# Configuration

Voici les informations de configuration pour votre réseau Wi-Fi et votre serveur MQTT.

## Wi-Fi Configuration

- **SSID**: `le ssid`
- **Mot de passe**: `la clé`

## MQTT Configuration

- **Adresse du broker MQTT**: `l'adresse IP`
- **Topic MQTT**: `le topic`
- **Utilisateur MQTT**: `le compte user`
- **Mot de passe MQTT**: `mon_mdp`


