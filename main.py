import telebot
import requests
from io import BytesIO

TOKEN = '8749511132:AAFWHiE-Qusrwl3UtC-dxU7PDAZIK4Pcuus'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'nazar'])
def send_map(message):
    # هذا الرابط هو المصدر الجديد والشغال 100% حالياً
    img_url = "https://jeanropke.github.io/RDR2CollectorsMap/assets/images/nazar.png"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(img_url, headers=headers, timeout=15)
        if response.status_code == 200:
            # يرسل الصورة مباشرة للمحادثة
            bot.send_photo(message.chat.id, BytesIO(response.content), caption="📍 موقع مدام نزار (خريطة حية)")
        else:
            # إذا السيرفر انحظر، يرسل الرابط كرسالة وتيليجرام يظهر المعاينة
            bot.send_message(message.chat.id, f"الموقع محمي، شوفي الخريطة هنا:\n{img_url}")
    except:
        bot.reply_to(message, "السيرفر مضغوط، جربي مرة ثانية.")

if __name__ == "__main__":
    bot.infinity_polling()
    
