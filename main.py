import telebot
import requests
from io import BytesIO

TOKEN = '8749511132:AAFWHiE-Qusrwl3UtC-dxU7PDAZIK4Pcuus'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'nazar'])
def send_map(message):
    bot.reply_to(message, "جاري تحديد موقع مدام نزار على الخريطة... 📍")
    
    # روابط الصور المباشرة (نجرب أكثر من واحد)
    urls = [
        "https://madamnazar.io/images/map.png",
        "https://jeanropke.github.io/RDOMap/assets/images/nazar.png"
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    success = False
    for img_url in urls:
        try:
            response = requests.get(img_url, headers=headers, timeout=15)
            if response.status_code == 200:
                photo = BytesIO(response.content)
                bot.send_photo(message.chat.id, photo, caption="هذا موقعها اليوم بالدبوس! 💃")
                success = True
                break
        except:
            continue

    if not success:
        bot.reply_to(message, "الموقع الرسمي للصورة محمي حالياً، يمكنك رؤيتها هنا: https://madamnazar.io/")

if __name__ == "__main__":
    bot.infinity_polling()
    
    except Exception as e:
        bot.reply_to(message, "فيه مشكلة بالاتصال، تأكدي إن السيرفر شغال.")

if __name__ == "__main__":
    bot.infinity_polling()
    
