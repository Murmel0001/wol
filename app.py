import subprocess
from flask import Flask

app = Flask(__name__)

def run_wol_bash_script():
    try:
        # Führe das Bash-Skript aus, das das Wake-on-LAN-Paket sendet
        subprocess.run(["./wol.sh"], check=True)
        return "Wake-on-LAN packet has been sent!"
    except subprocess.CalledProcessError as e:
        return f"An error occurred while running the Bash script: {e}"

@app.route('/')
def home():
    result = run_wol_bash_script()
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
