import yaml
import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters

# Функция для получения предсказания от модели (пример)
def get_prediction_from_model(text: str) -> float:
    # Здесь должна быть логика получения предсказания от вашей модели
    # В данном примере возвращаем случайное значение для демонстрации
    import random
    return random.uniform(0, 1)

# Функция для обработки команды /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! I am your stock prediction bot. Send me a company name.')

# Функция для обработки текстовых сообщений
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    # Получение предсказания от модели
    prediction = get_prediction_from_model(text)
    
    # Определение порогов для рекомендаций
    if prediction > 0.6:
        response = "Покупаем"
    elif prediction < 0.4:
        response = "Продаем"
    else:
        response = "Ждем"

    # Отправка ответа пользователю
    await update.message.reply_text(f'Предсказание: {prediction:.2f}\nРекомендация: {response}')

async def main() -> None:
    config_path = 'config/config.yaml'

    # Проверка существования файла
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    # Загрузка конфигурации
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
        print("Loaded configuration:", config)  # Вывод содержимого конфигурации

    # Проверка структуры конфигурации
    if 'telegram' not in config:
        print("Available keys:", config.keys())  # Вывод доступных ключей
        raise KeyError("'telegram' key not found in configuration file")

    if 'api_key' not in config['telegram']:
        raise KeyError("'api_key' key not found in 'telegram' section")

    # Получение токена из конфигурации
    TOKEN = config['telegram']['api_key']
    print(f"Token: {TOKEN}")

    # Создание приложения
    application = Application.builder().token(TOKEN).build()

    # Регистрация обработчиков команд и сообщений
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    await application.run_polling()

if __name__ == '__main__':
    # Запуск приложения в стандартном цикле событий
    asyncio.run(main())




   






