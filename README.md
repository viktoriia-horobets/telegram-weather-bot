# telegram-weather-bot
Telegram bot that provides current weather information.  
Dockerized, CI/CD-ready, and deployed via Kubernetes and Render

Try it:
Telegram: [@myweather01_bot](https://t.me/myweather01_bot)  

Tech Stack
- **Python** (telegram-bot, requests, dotenv)
- **Docker** (containerized app)
- **GitHub Actions** (CI/CD, auto-build + push to DockerHub)
- **DockerHub** (image hosting)
- **Kubernetes** (local `kind` deployment)
- **Render** (free-tier cloud deployment)
- **OpenWeatherMap API** (for weather data)

Features
- `/start` — welcome message
- `/weather <city>` — returns current weather
- Uses Telegram Bot API and OpenWeatherMap
- Deployed and scalable via Docker & Kubernetes

# Install dependencies
pip install -r requirements.txt

# Run the bot
python bot.py

Docker:
docker build -t telegram-weather-bot .
docker run --env-file .env telegram-weather-bot

Kubernetes (local kind):
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/deployment.yaml
kubectl get pods

CI/CD GitHub Actions pipeline:
- Build on push to main
- Push image to DockerHub
- Auto-deploy via Render
