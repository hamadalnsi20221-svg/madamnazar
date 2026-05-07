import telebot
import requests
import logging
from datetime import datetime
from pytz import timezone
import os
from dotenv import load_dotenv
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import hashlib
from PIL import Image
from io import BytesIO

# تحميل متغيرات البيئة
load_dotenv()
BOT_TOKEN = os.getenv('8372609971:AAFt0f-BZLIbkREnAAY2wp_3g5eA-1siQSU')
CHANNEL_ID = os.getenv('-1003763689916')
API_URL = "https://api.madamnazar.io"

# إعدادات السجلات
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# إنشاء نسخة من telebot مع خيارات مخصصة
bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')

# توقيت السعودية
saudi_tz = timezone('Asia/Riyadh')

class MadamNazarAPI:
    """فئة للتعامل مع API مع ميزات Cache Busting والاتصال الموثوق"""
    
    def __init__(self, api_url):
        self.api_url = api_url
        self.session = self._create_session()
        self.last_location = None
        self.last_fetch_time = None
    
    def _create_session(self):
        """إنشاء جلسة requests مع Retry Strategy مخصصة"""
        session = requests.Session()
        
        # استراتيجية إعادة المحاولة
        retry_strategy = Retry(
            total=5,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["HEAD", "GET", "OPTIONS"]
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # إضافة User-Agent مخصص
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        return session
    
    def _get_cache_buster(self):
        """إنشاء cache buster متغير (تاريخ اليوم بتوقيت السعودية)"""
        saudi_now = datetime.now(saudi_tz)
        return saudi_now.strftime("%Y-%m-%d-%H")
    
    def fetch_location(self, retries=3):
        
