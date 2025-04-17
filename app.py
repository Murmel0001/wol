from flask import Flask
import socket

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
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(data, (TARGET_IP, 9))  # Ziel-IP und Port 9 für WoL-Paket

@app.route('/')
def home():
    return "Flask is running!"

@app.route('/wake', methods=['GET'])
def wake():
    try:
        send_wol()
        return f"WOL packet sent to {MAC_ADDRESS} at IP {TARGET_IP}", 200
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
