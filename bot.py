from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# === CONFIGURAÇÕES ===
TOKEN = '7590060529:AAE0eybJPn18uAAh1Z7hMSFI0ESovEXl_m4'

CANAL_URL = "https://t.me/MarcusTraderOficial"
INSTAGRAM_URL = "https://www.instagram.com/dovalemarcus/"
SETUP_URL = "https://t.me/MarcusTraderOficial/2"  # Substitua se quiser outro link

# === MENSAGEM DE BOAS-VINDAS ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Canal de Sinais", url=CANAL_URL)],
        [InlineKeyboardButton("📸 Instagram Oficial", url=INSTAGRAM_URL)],
        [InlineKeyboardButton("📚 Entender os Setups", url=SETUP_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Fala, Trader! Seja bem-vindo ao universo Marcus Trader 📈\n\n"
        "Aqui você pode acessar:\n"
        "🔗 Canal de sinais gratuitos\n"
        "🎥 Lives com entradas comentadas\n"
        "📚 Conteúdo para elevar sua leitura de mercado\n\n"
        "Clique abaixo 👇",
        reply_markup=reply_markup
    )

# === APLICAÇÃO ===
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, start))  # responde a qualquer texto
    print("✅ Bot rodando. Pressione Ctrl+C para encerrar.")
    app.run_polling()
