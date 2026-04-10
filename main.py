import telebot
import requests
from io import BytesIO

TOKEN = '8749511132:AAFWHiE-Qusrwl3UtC-dxU7PDAZIK4Pcuus'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'nazar'])
def send_map(message):
    bot.reply_to(message, "📍 لحظة.. جاري سحب الخريطة المحدثة بالدبوس...")
    
    urls = [
        "https://raw.githubusercontent.com/bounca/madamnazar/master/map.png",
        "https://www.madamnazar.io/images/map.png"
    ]
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    success = False
    for url in urls:
        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code == 200:
                bot.send_photo(message.chat.id, BytesIO(res.content), caption="📍 هذي هي الخريطة وعليها موقعها بالضبط!")
                success = True
                break
        except:
            continue
            
    if not success:
        bot.send_message(message.chat.id, "المواقع الرسمية معلقة، شوفيها من الرابط المباشر:\nhttps://madamnazar.io/")

if __name__ == "__main__":
    bot.infinity_polling()
