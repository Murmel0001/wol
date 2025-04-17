from flask import Flask, request
import socket

app = Flask(__name__)

def send_wol(mac_address):
    mac_address = mac_address.replace(":", "").replace("-", "")
    if len(mac_address) != 12:
        raise ValueError("MAC address format is invalid")

    data = bytes.fromhex("FF" * 6 + mac_address * 16)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(data, ("<broadcast>", 9))

@app.route('/wake', methods=['GET'])
def wake():
    mac = request.args.get('mac')
    if not mac:
        return "MAC address missing, use /wake?mac=00:11:22:33:44:55", 400
    try:
        send_wol(mac)
        return f"WOL packet sent to {mac}", 200
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
