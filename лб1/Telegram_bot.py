from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    commands = """
    Вітаю! Я Telegram-бот. Ось команди:
/menu - меню 
/whisper - "Ти тихий🤫"
/scream - "Ти гучний😱"
    """
    await update.message.reply_text(commands)
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    commands = """
    Доступні команди:
/menu - меню 
/whisper - "Ти тихий🤫"
/scream - "Ти гучний😱"
    """
    await update.message.reply_text(commands)
async def whisper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Ти тихий 🤫")
async def scream(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Ти гучний 😱")


def main():
    token = 'bot_token_from_BotFather'
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("whisper", whisper))
    app.add_handler(CommandHandler("scream", scream))
    print("Бот запустився")
    app.run_polling()
if __name__ == "__main__":
    main()