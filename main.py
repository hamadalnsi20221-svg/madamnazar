import telebot

# التوكن حقك
TOKEN = '8749511132:AAFWHiE-Qusrwl3UtC-dxU7PDAZIK4Pcuus'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'nazar'])
def send_location(message):
    # رسالة واضحة وبرابط مباشر يشتغل 100%
    text = (
        "💃 **موقع مدام نزار اليوم:**\n\n"
        "المواقع حالياً تمنع إرسال الصور مباشرة، لكن تقدرين تشوفين مكانها بدقة عالية من هنا:\n"
        "🔗 https://madamnazar.io/\n\n"
        "أو الخريطة التفاعلية الشاملة:\n"
        "🔗 https://jeanropke.github.io/RDOMap/"
    )
    bot.reply_to(message, text, parse_mode='Markdown')

if __name__ == "__main__":
    print("البوت شغال الحين..")
    bot.infinity_polling()
    
