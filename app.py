from flask import Flask
import socket
import time

app = Flask(__name__)

# MAC-Adresse und Ziel-IP-Adresse fest im Code definiert
MAC_ADDRESS = "BC:FC:E7:1A:CC:6F"
TARGET_IP = "192.168.10.11"

def send_wol():
    mac_address = MAC_ADDRESS.replace(":", "").replace("-", "")
    if len(mac_address) != 12:
        raise ValueError("MAC address format is invalid")

    # Wake-on-LAN-Paket vorbereiten
    data = bytes.fromhex("FF" * 6 + mac_address * 16)
    
    # Sende das WoL-Paket 3-mal hintereinander
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        for _ in range(3):  # Sende 3-mal
            s.sendto(data, ("<broadcast>", 9))  # Ziel-IP und Port 9 für WoL-Paket
            print(f"WOL packet sent to {MAC_ADDRESS} at IP {TARGET_IP}")
            time.sleep(1)  # Kurze Pause von 1 Sekunde zwischen den Versuchen

@app.route('/')
def home():
    return "Flask is running and WOL packet has been sent!"

if __name__ == '__main__':
    # Wake-on-LAN direkt beim Start ausführen
    try:
        send_wol()
        print(f"WOL packet sent")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    app.run(host='0.0.0.0', port=8888)
