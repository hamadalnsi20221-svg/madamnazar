import telebot
import requests
from io import BytesIO

# التوكن الخاص بك
TOKEN = '8749511132:AAFWHiE-Qusrwl3UtC-dxU7PDAZIK4Pcuus'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'nazar'])
def send_location(message):
    bot.reply_to(message, "لحظة أشوف لك وين مختفية مدام نزار اليوم... 🔍")
    
    # رابط الصورة من مصدر بديل ومستقر (Jean Ropke)
    image_url = "https://jeanropke.github.io/RDOMap/assets/images/nazar.png"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # محاولة سحب الصورة
        response = requests.get(image_url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            photo = BytesIO(response.content)
            bot.send_photo(
                message.chat.id, 
                photo, 
                caption="هذا هو موقع مدام نزار الحالي! 💃✨\n\nالموقع يتحدث يومياً."
            )
        else:
            # لو فشل المصدر البديل، نحاول نرسل رابط الموقع ككتابة
            bot.reply_to(message, "عذراً، الخريطة كصورة غير متوفرة حالياً، يمكنك رؤيتها هنا: https://jeanropke.github.io/RDOMap/")
            
    except Exception as e:
        bot.reply_to(message, "واجهت مشكلة في الاتصال بالموقع، جربي لاحقاً.")

if __name__ == "__main__":
    bot.infinity_polling()
    
