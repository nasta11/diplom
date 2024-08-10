import yaml
import os
import asyncio
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters

# Функция для получения предсказания от модели (пример)
def get_prediction_from_model(text: str) -> float:
    import random
    return random.uniform(0, 1)

# Функция для обработки команды /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Я ваш бот для предсказания акций. Отправьте мне название компании.')

# Функция для обработки текстовых сообщений
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    prediction = get_prediction_from_model(text)
    
    if prediction > 0.6:
        response = "Покупаем"
    elif prediction < 0.4:
        response = "Продаем"
    else:
        response = "Ждем"

    await update.message.reply_text(f'Предсказание: {prediction:.2f}\nРекомендация: {response}')

async def main() -> None:
    config_path = 'config/config.yaml'

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
        print("Loaded configuration:", config)

    telegram_config = config.get('telegram', {})
    TOKEN = telegram_config.get('api_key')

    if not TOKEN:
        raise KeyError("'api_key' key not found in 'telegram' section")

    print(f"Token: {TOKEN}")

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

    # Ожидание завершения работы
    try:
        while True:
            await asyncio.sleep(3600)  # Ожидание с интервалом в 1 час
    except KeyboardInterrupt:
        print("Bot stopped manually")

if __name__ == "__main__":
    if sys.platform.startswith('win') and sys.version_info >= (3, 8):
        import asyncio
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # Запуск основного цикла
    asyncio.run(main())

   






