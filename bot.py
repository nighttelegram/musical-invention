import os
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    InputMediaPhoto
)
from telegram.constants import ChatAction
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# === CONTADOR DE USUÁRIOS QUE INICIARAM O BOT ===
def ler_contador():
    if not os.path.exists("contador.txt"):
        with open("contador.txt", "w") as f:
            f.write("0")
    with open("contador.txt", "r") as f:
        return int(f.read())

def incrementar_contador():
    contador = ler_contador() + 1
    with open("contador.txt", "w") as f:
        f.write(str(contador))
    return contador

# === CONTADOR DE CLIQUES NO BOTÃO QUERO MEU ACESSO ===
def ler_contador_acessos():
    if not os.path.exists("contador_acessos.txt"):
        with open("contador_acessos.txt", "w") as f:
            f.write("0")
    with open("contador_acessos.txt", "r") as f:
        return int(f.read())

def incrementar_contador_acessos():
    contador = ler_contador_acessos() + 1
    with open("contador_acessos.txt", "w") as f:
        f.write(str(contador))
    return contador

# === /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contador = incrementar_contador()
    user = update.effective_user
    nome = user.full_name
    username = user.username if user.username else "sem @"

    print(f"[ACESSO] {nome} (@{username}) iniciou o bot. Total de acessos: {contador}")

    keyboard = [[InlineKeyboardButton("QUERO ENTENDER MELHOR", callback_data="entender")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

    with open("ftbot.jpeg", "rb") as photo:  # Imagem no mesmo diretório
        await update.message.reply_photo(
            photo=photo,
            caption=(
                "Olá, tudo bem? Vou te explicar como funciona o nosso aplicativo: O APP Espião é um aplicativo de "
                "monitoramento passo a passo para você que suspeita que o seu amor está te traindo, ou para você que "
                "já sabe que está sendo traído(a) e não tem provas. Também serve para monitorar o celular dos seus filhos. "
                "Com o App você poderá ter acesso ao WhatsApp do seu parceiro em tempo real sem que ele saiba, apenas "
                "colocando o número dele no App Espião, sem precisar ter o celular do seu parceiro."
            ),
            reply_markup=reply_markup
        )

# === Botões ===
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await context.bot.send_chat_action(chat_id=query.message.chat_id, action=ChatAction.TYPING)

    if query.data == "entender":
        keyboard = [[InlineKeyboardButton("QUERO MEU ACESSO", callback_data="acesso")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_caption(
            caption="O espião do amor usa uma técnica poderosa de webhacking capaz de invadir até os dispositivos mais seguros e protegidos, sendo a melhor ferramenta disponível no mercado.",
            reply_markup=reply_markup
        )

    elif query.data == "acesso":
        contador_acessos = incrementar_contador_acessos()
        print(f"[ACESSO] Botão QUERO MEU ACESSO clicado. Total: {contador_acessos}")

        with open("ftbot.jpeg", "rb") as photo:
            await query.edit_message_media(
                media=InputMediaPhoto(
                    media=photo,
                    caption="✅ Você está quase lá!"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("quero meu acesso", url="https://t.me/Padrinho71")]]
                )
            )

# === Inicializa o bot ===
def main():
    app = Application.builder().token("COLOQUE_SEU_TOKEN_AQUI").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot rodando... Pressione Ctrl+C para parar.")
    app.run_polling()

if __name__ == "__main__":
    main()
