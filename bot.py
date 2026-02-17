import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    if message.voice.duration > 15:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(
            message.chat.id,
            f"{message.from_user.first_name}, придержи коней, ковбой! MAX 15sec"
        )

bot.polling()
