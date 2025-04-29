import os
import requests
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    force=True
)


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}&units=metric&lang=ua"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        return f"Погода в {city_name}: {temp}°C, {description}"
    else:
        return "Не вдалося отримати погоду. Перевірте правильність назви міста."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info(f"User {update.effective_user.id} started the bot.")
    await update.message.reply_text(
        "Привіт! 👋 Я бот погоди. Надішли мені /weather <місто> і я скажу тобі прогноз!"
    )


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Будь ласка, введи місто після команди /weather.")
        return
    city_name = " ".join(context.args)
    logging.info(f"User {update.effective_user.id} requested weather for {city_name}.")
    weather_info = get_weather(city_name)
    await update.message.reply_text(weather_info)


app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("weather", weather))

def main():
    app.run_polling()

if __name__ == "__main__":
    main()