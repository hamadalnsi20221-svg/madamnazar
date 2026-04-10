import telebot
import requests
from io import BytesIO


TOKEN = '8749511132:AAFWHiE-Qusrwl3UtC-dxU7PDAZIK4Pcuus'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'nazar'])
def send_map(message):
    bot.reply_to(message, "لحظة.. جاري سحب الخريطة وتحديد موقع مدام نزار 📍")
    
    
    img_url = "https://madamnazar.io/images/map.png"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(img_url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            
            photo = BytesIO(response.content)
            bot.send_photo(
                message.chat.id, 
                photo, 
                caption="هذا هو موقع مدام نزار لليوم (الخريطة محدثة) ✨"
            )
        else:
            alt_url = "https://jeanropke.github.io/RDOMap/assets/images/nazar.png"
            res_alt = requests.get(alt_url, headers=headers)
            if res_alt.status_code == 200:
                bot.send_photo(message.chat.id, BytesIO(res_alt.content), caption="تم سحب الخريطة من المصدر البديل! 📍")
            else:
                bot.reply_to(message, "للأسف المواقع الرسمية قافلة سحب الصور حالياً، جربي بعد شوي.")
                
    except Exception as e:
        bot.reply_to(message, "فيه مشكلة بالاتصال، تأكدي إن السيرفر شغال.")

if __name__ == "__main__":
    bot.infinity_polling()
    
