import telebot
import requests
from io import BytesIO

TOKEN = '8749511132:AAFWHiE-Qusrwl3UtC-dxU7PDAZIK4Pcuus'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'nazar'])
def send_location(message):
    bot.reply_to(message, "لحظة أشوف لك وين مختفية مدام نزار اليوم... 🔍")
    
    # رابط الصورة العالمي لموقع مدام نزار
    image_url = "https://madamnazar.io/images/map.png"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(image_url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            photo = BytesIO(response.content)
            bot.send_photo(
                message.chat.id, 
                photo, 
                caption="هذا هو موقع مدام نزار الحالي! 💃✨\n\nالموقع يتحدث تلقائياً كل 24 ساعة."
            )
        else:
            bot.reply_to(message, f"الموقع رفض يعطيني الخريطة (Error: {response.status_code}). جربي مرة ثانية بعد شوي.")
            
    except Exception as e:
        bot.reply_to(message, "واجهت مشكلة تقنية في الوصول للخريطة.")

# تشغيل البوت
if __name__ == "__main__":
    print("البوت بدأ العمل بنجاح...")
    bot.infinity_polling()
