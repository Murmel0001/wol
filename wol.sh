#!/bin/bash

# MAC-Adresse und Ziel-IP fest im Code
MAC_ADDRESS="BC:FC:E7:1A:CC:6F"
TARGET_IP="192.168.10.11"

# MAC-Adresse ohne Trennzeichen
MAC_ADDRESS=$(echo $MAC_ADDRESS | tr -d ':' | tr -d '-')

# Wake-on-LAN-Paket senden (UDP auf Port 9)
echo "Sending Wake-on-LAN packet to $MAC_ADDRESS at $TARGET_IP"

# Sende WoL-Paket 3-mal hintereinander
for i in {1..3}
do
    wakeonlan $MAC_ADDRESS
    echo "WoL packet sent - Attempt $i"
    sleep 1  # Warte 1 Sekunde zwischen den Versuchen
done
