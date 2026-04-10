import telebot
import requests

TOKEN = '8749511132:AAFWHiE-Qusrwl3UtC-dxU7PDAZIK4Pcuus'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'nazar'])
def get_nazar_location(message):
    bot.reply_to(message, "لحظة أتواصل مع الرادار الخاص بمدام نزار... 📡")
    
    try:
        # استخدام API بديل يسحب الموقع كنص
        api_url = "https://api.madamnazar.io/location/current"
        response = requests.get(api_url, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            # سحب اسم المنطقة والمنطقة الكبرى
            location_name = data.get('data', {}).get('name', 'غير معروف')
            region = data.get('data', {}).get('region', {}).get('name', 'غير معروف')
            
            msg = (
                f"📍 **موقع مدام نزار الحالي:**\n\n"
                f"🏘 **المنطقة:** {location_name}\n"
                f"🌍 **الإقليم:** {region}\n\n"
                f"🔗 **للخريطة:** https://madamnazar.io/"
            )
            bot.reply_to(message, msg, parse_mode='Markdown')
        else:
            # إذا فشل الـ API، نرسل الرابط مباشرة كحل أخير
            bot.reply_to(message, "الموقع يرفض السحب المباشر حالياً، شوفيها هنا: https://madamnazar.io/")
            
    except Exception as e:
        bot.reply_to(message, "الموقع الرسمي عليه ضغط، جربي الرابط: https://madamnazar.io/")

if __name__ == "__main__":
    bot.infinity_polling()
    
