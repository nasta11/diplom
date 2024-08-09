import yaml
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import asyncio

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! I am your bot.')

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

    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    await application.run_polling()

if __name__ == '__main__':
    # Запуск приложения в стандартном цикле событий
    asyncio.run(main())




   






