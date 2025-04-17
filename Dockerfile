# Verwende ein offizielles Python-Image als Basis
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Kopiere die benötigten Dateien ins Container-Verzeichnis
COPY . /app

# Installiere die Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Mache das Bash-Skript ausführbar
RUN chmod +x wol.sh

# Exponiere Port 8888
EXPOSE 8888

# Starte die Flask-App
CMD ["python", "app.py"]
