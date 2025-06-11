# USDT Telegram Bot on BSC
بوت تليجرام بسيط لعرض رصيد USDT على شبكة Binance Smart Chain (BSC) وآخر 10 معاملات.

## كيفية التشغيل
1. أنشئ ملف `.env` أو استخدم متغيرات بيئة:
   - `BOT_TOKEN`: توكن بوت التليجرام
   - `BSC_API_KEY`: مفتاح BscScan

2. ثبت المتطلبات:
```
pip install -r requirements.txt
```

3. شغّل البوت:
```
python usdt_bot.py
```

## الميزات
- عرض رصيد USDT (BEP-20)
- عرض آخر 10 معاملات
