import telebot

TOKEN = "8052561079:AAFyfICJJQrpPQaV4PDYnBLCw9_snkSqf2k"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Merhaba! Kripto Sinyal Botu çalışıyor ✅")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Gelen mesaj: {message.text}")

print("Bot çalışıyor...")
bot.infinity_polling()
