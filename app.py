from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

TOKEN = 8727058246:AAEFrkEm8ArS3MIoIy8ldAdMJhVPczzUyVs

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🦋 Bot encendido. Bienvenida a Moonlight Bloom 🦋")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot encendido 🦋")
app.run_polling()