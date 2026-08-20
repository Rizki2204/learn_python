from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot-nya jalan!")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hai, dengan siapa disini?")    

app = ApplicationBuilder().token("8272041378:AAHRbaKhjQsdd1QwGQWhp0_ccYXOiGTLSDU").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("about", about))
app.run_polling()