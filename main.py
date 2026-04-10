import telebot
import requests
from io import BytesIO

TOKEN = '8749511132:AAFWHiE-Qusrwl3UtC-dxU7PDAZIK4Pcuus'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'nazar'])
def send_map(message):
    # الرابط المباشر للخريطة (المصدر اللي ما يعطي 404)
    img_url = "https://jeanropke.github.io/RDR2CollectorsMap/assets/images/nazar.png"
    
    # السر هنا: نغير الهوية عشان ريندر ما ينكشف
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1'
    }

    try:
        response = requests.get(img_url, headers=headers, timeout=15)
        if response.status_code == 200:
            # يرسل الصورة مباشرة
            bot.send_photo(message.chat.id, BytesIO(response.content), caption="📍 موقع مدام نزار اليوم")
        else:
            # لو الحظر لسه موجود، نرسل الرابط بطريقة تجبر تليجرام يعرض الصورة
            bot.send_message(message.chat.id, f"المواقع الرسمية قافلة السحب، شوفيها هنا:\n{img_url}")
    except:
        bot.reply_to(message, "السيرفر معلق، جربي مرة ثانية.")

if __name__ == "__main__":
    bot.infinity_polling()
    
