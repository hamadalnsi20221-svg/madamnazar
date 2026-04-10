import telebot
import requests
from io import BytesIO

TOKEN = '8749511132:AAFWHiE-Qusrwl3UtC-dxU7PDAZIK4Pcuus'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'nazar'])
def send_map(message):
    bot.reply_to(message, "لحظة.. أجيب لك الخريطة من المصدر الشغال 📍")
    
    img_url = "https://jeanropke.github.io/RDOMap/assets/images/nazar.png"
    
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(img_url, headers=headers, timeout=15)
        if response.status_code == 200:
            bot.send_photo(message.chat.id, BytesIO(response.content), caption="📍 هذي هي الخريطة وعليها الدبوس!")
        else:
            bot.reply_to(message, "المصدر الرسمي فيه مشكلة حالياً، جربي بعد دقيقة.")
    except:
        bot.reply_to(message, "تأكدي من اتصال السيرفر.")

if __name__ == "__main__":
    bot.infinity_polling()
