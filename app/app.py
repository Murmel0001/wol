from flask import Flask, render_template
import socket
import os

app = Flask(__name__, template_folder='templates')

MAC_ADDRESS = os.environ.get("MAC_ADDRESS", "")

def send_wol(mac):
    addr_byte = bytes.fromhex(mac.replace(':', '').replace('-', ''))
    magic_packet = b'\xff' * 6 + addr_byte * 16
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(magic_packet, ('<broadcast>', 9))
    print(f"WOL-Paket an {mac} gesendet")

@app.route('/wol')
def wol():
    try:
        send_wol(MAC_ADDRESS)
        return "WOL gesendet"
    except Exception as e:
        print("Fehler beim WOL:", e)
        return "Fehler beim Senden", 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
