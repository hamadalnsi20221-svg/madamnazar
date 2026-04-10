import telebot
import requests
from io import BytesIO

TOKEN = '8749511132:AAFWHiE-Qusrwl3UtC-dxU7PDAZIK4Pcuus'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'nazar'])
def send_map(message):
    # رابط خريطة جان روبكي (الأضمن حالياً)
    img_url = "https://jeanropke.github.io/RDOMap/assets/images/nazar.png"
    
    # نغير الـ Headers عشان نخدع الموقع
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'
    }

    try:
        response = requests.get(img_url, headers=headers, timeout=15)
        if response.status_code == 200:
            bot.send_photo(message.chat.id, BytesIO(response.content), caption="📍 جبتها لك من المصدر البديل!")
        else:
            # إذا فشل السحب، نرسل الرابط مباشرة والتيليجرام بيعرض الصورة غصب
            bot.send_message(message.chat.id, f"المواقع الرسمية قافلة السحب، شوفي الخريطة هنا:\n\n{img_url}")
    except:
        bot.send_message(message.chat.id, "المعذرة، حاولي مرة ثانية بعد ثواني.")

if __name__ == "__main__":
    bot.infinity_polling()
    
