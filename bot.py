from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Sim", callback_data="sim")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Olá seja bem vindo(a) ao Espia do Amor deseja prosseguir",
        reply_markup=reply_markup
    )

# Lida com os botões
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "sim":
        keyboard = [[InlineKeyboardButton("Prosseguir", callback_data="prosseguir")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "O espião do amor e uma ferramenta inovadora para você conseguir descubrir todas as conversas de qualquer whatsapp de qualquer pessoa 👇👇👇👇👇",
            reply_markup=reply_markup
        )
    elif query.data == "prosseguir":
        await query.edit_message_text(
            "✅ Você está quase lá! Use o comando /nu e o numero desejado para clonar a conversac."
        )

# Comando /nu
async def nu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔒 Para revelar a conversa, pague a taxa de **R$60,00**."
    )

# Inicializa o bot
def main():
    app = Application.builder().token("7826889737:AAEXfwuvy7exTIPh4v8lqxnrdWyM_NGgpOc").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler("nu", nu))

    print("Bot rodando... Pressione Ctrl+C para parar.")
    app.run_polling()

if __name__ == "__main__":
    main()
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Sim", callback_data="sim")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Você deseja saber o que é o Espião do Amor?",
        reply_markup=reply_markup
    )

# Lida com os botões
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "sim":
        keyboard = [[InlineKeyboardButton("Prosseguir", callback_data="prosseguir")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🕵️‍♂️ O Espião do Amor é uma ferramenta secreta que te ajuda a descobrir se alguém gosta de você 💘",
            reply_markup=reply_markup
        )
    elif query.data == "prosseguir":
        await query.edit_message_text(
            "✅ Você está quase lá! Use o comando /nu para continuar."
        )

# Comando /nu
async def nu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔒 Para revelar a conversa, pague a taxa de **R$60,00**."
    )

# Inicializa o bot
def main():
    app = Application.builder().token("7826889737:AAEXfwuvy7exTIPh4v8lqxnrdWyM_NGgpOc").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler("nu", nu))

    print("Bot rodando... Pressione Ctrl+C para parar.")
    app.run_polling()

if __name__ == "__main__":
    main()
