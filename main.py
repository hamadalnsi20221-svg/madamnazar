import telebot
import requests
from io import BytesIO

TOKEN = '8749511132:AAFWHiE-Qusrwl3UtC-dxU7PDAZIK4Pcuus'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'nazar'])
def send_map(message):
    bot.reply_to(message, "لحظة بجيب لك الخريطة من المصدر المفتوح... 📍")
    
    
    img_url = "https://raw.githubusercontent.com/bounca/madamnazar/master/map.png"
    
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(img_url, headers=headers, timeout=15)
        if response.status_code == 200:
            bot.send_photo(message.chat.id, BytesIO(response.content), caption="لقيتها! هذي الخريطة بالدبوس 💃")
        else:
            bot.reply_to(message, "الموقع الرسمي حظر السيرفر، شوفيها هنا مباشرة:\nhttps://madamnazar.io/images/map.png")
    except:
        bot.reply_to(message, "فيه مشكلة فنية، جربي بعد دقيقة.")

if __name__ == "__main__":
    bot.infinity_polling()
    
