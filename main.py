import telebot

TOKEN = '8749511132:AAFWHiE-Qusrwl3UtC-dxU7PDAZIK4Pcuus'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'nazar'])
def send_map(message):
    map_url = "https://madamnazar.io/images/map.png"
    
    try:
        bot.send_photo(message.chat.id, map_url, caption="📍 موقع مدام نزار اليوم")
    except:
        bot.send_message(message.chat.id, f"📍 تفضلي الخريطة:\n\n{map_url}")

if __name__ == "__main__":
    bot.infinity_polling()
