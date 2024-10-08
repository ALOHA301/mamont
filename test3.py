from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

# Функция для команды /start
async def start(update: Update, context: CallbackContext) -> None:
    # URL для твоей игры
    web_app_url = "https://aloha301.github.io/mamont/"
    
    # Создаём кнопку для запуска веб-приложения
    keyboard = [
        [InlineKeyboardButton("Играть в Mammoth Tapper", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправляем сообщение с приветствием и кнопкой
    await update.message.reply_text(f"Привет, {update.effective_user.first_name}! Тапай на мамонта, чтобы заработать GOYкоины!", reply_markup=reply_markup)

# Токен твоего бота
TOKEN = "7772716151:AAGiMQaFDqrp64_2cAUfwcLJOFk2TInaOt8"

# Создаём приложение бота
app = ApplicationBuilder().token(TOKEN).build()

# Добавляем обработчик команды /start
app.add_handler(CommandHandler("start", start))

# Запускаем бота
app.run_polling()
