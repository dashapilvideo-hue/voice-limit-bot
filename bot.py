import os
import telebot

TOKEN = os.environ.get("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN not found!")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    try:
        if message.voice.duration > 15:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(
                message.chat.id,
                f"{message.from_user.first_name}, голосовые сообщения должны быть не длиннее 15 секунд!"
            )
    except Exception as e:
        print(f"Error: {e}")

print("Bot started...")
bot.infinity_polling()
