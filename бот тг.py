from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN = "8588098984:AAHVQNrC7A9fgWI0myuSj-81eon7_2_jVyo"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("привет я бот которого зовут алексей навальный ")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(f"вы написали: {user_text}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("команды навльного:\n/start - начать общение\n/help - помощь")

def main():
    
    application = Application.builder().token(TOKEN).build()
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
   
    print("Бот опущен...")
    application.run_polling()

if __name__ == '__main__':
    main()
                
