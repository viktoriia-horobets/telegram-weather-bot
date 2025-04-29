FROM python:3.11-slim

WORKDIR /app

# Install socat
RUN apt-get update && apt-get install -y socat && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

# Expose health port
EXPOSE 8080

# Start both socat and your bot
CMD socat TCP-LISTEN:8080,fork,reuseaddr SYSTEM:'echo -e "HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n"' & \
    python bot.py