FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app

# Unprivilegierter Benutzer
RUN useradd -m woluser
USER woluser

EXPOSE 5000

CMD ["python", "app.py"]
