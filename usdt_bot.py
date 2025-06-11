import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# مفاتيح التليجرام و BSCScan
TELEGRAM_TOKEN = "توكن_البوت_بتاعك"
BSCSCAN_API_KEY = "مفتاح_BSCScan_بتاعك"

# دالة تجيب رصيد USDT من عنوان BSC
def get_usdt_balance(address):
    url = f"https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=0x55d398326f99059fF775485246999027B3197955&address={address}&tag=latest&apikey={BSCSCAN_API_KEY}"
    response = requests.get(url)
    data = response.json()
    balance = int(data["result"]) / 10**18
    return round(balance, 2)

# دالة تجيب آخر 10 معاملات
def get_transactions(address):
    url = f"https://api.bscscan.com/api?module=account&action=tokentx&address={address}&contractaddress=0x55d398326f99059fF775485246999027B3197955&page=1&offset=10&sort=desc&apikey={BSCSCAN_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("result", [])

# دالة تنفيذ الأمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 أهلا بيك! أرسل ليا عنوان محفظتك (BSC address) علشان أجيب ليك الرصيد والمعاملات.")

# دالة استلام العنوان وجلب البيانات
async def handle_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    address = update.message.text.strip()
    if address.startswith("0x") and len(address) == 42:
        try:
            usdt_balance = get_usdt_balance(address)
            txs = get_transactions(address)
            msg = f"📦 الرصيد: {usdt_balance} USDT\n\n📜 آخر 10 معاملات:\n"
            for tx in txs:
                from_addr = tx["from"]
                to_addr = tx["to"]
                amount = int(tx["value"]) / 10**18
                msg += f"🔹 {amount:.2f} USDT من {from_addr[:6]}... إلى {to_addr[:6]}...\n"
            await update.message.reply_text(msg)
        except Exception as e:
            await update.message.reply_text("🚫 حصل خطأ في جلب البيانات. جرّب تاني.")
    else:
        await update.message.reply_text("📛 العنوان ما صحيح. تأكد إنو بيبدأ بـ 0x وطولو 42 حرف.")

# تشغيل البوت
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("tx", handle_address))
    app.add_handler(CommandHandler("balance", handle_address))
    app.add_handler(CommandHandler("check", handle_address))
    app.add_handler(CommandHandler("address", handle_address))
    app.add_handler(CommandHandler("wallet", handle_address))
    app.add_handler(CommandHandler("محفظتي", handle_address))
    app.add_handler(CommandHandler("رصيدي", handle_address))
    app.add_handler(CommandHandler("تحقق", handle_address))
    app.add_handler(CommandHandler("استعلام", handle_address))
    app.add_handler(CommandHandler("معاملاتي", handle_address))
    app.add_handler(CommandHandler("balancebsc", handle_address))
    app.add_handler(CommandHandler("last10", handle_address))
    app.add_handler(CommandHandler("bsc", handle_address))
    app.add_handler(CommandHandler("bscscan", handle_address))
    app.add_handler(CommandHandler("walletbsc", handle_address))
    app.add_handler(CommandHandler("walletcheck", handle_address))
    app.add_handler(CommandHandler("bscwallet", handle_address))
    app.add_handler(CommandHandler("bscaddress", handle_address))
    app.add_handler(CommandHandler("balancecheck", handle_address))
    app.add_handler(CommandHandler("checkwallet", handle_address))
    app.add_handler(CommandHandler("bscbalance", handle_address))
    app.add_handler(CommandHandler("txs", handle_address))
    app.add_handler(CommandHandler("txlist", handle_address))
    app.add_handler(CommandHandler("txhistory", handle_address))
    app.add_handler(CommandHandler("transaction", handle_address))
    app.add_handler(CommandHandler("transactions", handle_address))
    app.add_handler(CommandHandler("show", handle_address))
    app.add_handler(CommandHandler("عرض", handle_address))
    app.add_handler(CommandHandler("بينات", handle_address))
    app.add_handler(CommandHandler("walletinfo", handle_address))
    app.add_handler(CommandHandler("walletstatus", handle_address))
    app.add_handler(CommandHandler("bscinfo", handle_address))
    app.add_handler(CommandHandler("addressinfo", handle_address))
    app.add_handler(CommandHandler("status", handle_address))
    app.add_handler(CommandHandler("الرصيد", handle_address))
    app.add_handler(CommandHandler("المعاملات", handle_address))
    app.add_handler(CommandHandler("تحويلات", handle_address))
    app.add_handler(CommandHandler("walletbscscan", handle_address))
    app.add_handler(CommandHandler("عرضالمعاملات", handle_address))
    app.add_handler(CommandHandler("showtx", handle_address))
    app.add_handler(CommandHandler("معاملات", handle_address))
    app.add_handler(CommandHandler("walletinfo", handle_address))
    app.add_handler(CommandHandler("txinfo", handle_address))
    app.add_handler(CommandHandler("checkbsc", handle_address))
    app.add_handler(CommandHandler("bscwalletinfo", handle_address))
    app.add_handler(CommandHandler("bscwalletstatus", handle_address))
    app.add_handler(CommandHandler("bsctx", handle_address))
    app.add_handler(CommandHandler("showwallet", handle_address))
    app.add_handler(CommandHandler("showbsc", handle_address))
    app.add_handler(CommandHandler("عرضالرصيد", handle_address))
    app.add_handler(CommandHandler("عرضالتحويلات", handle_address))
    app.add_handler(CommandHandler("تفاصيل", handle_address))
    app.add_handler(CommandHandler("بيانات", handle_address))
    app.add_handler(CommandHandler("checkbscwallet", handle_address))
    app.add_handler(CommandHandler("checkaddress", handle_address))
    app.add_handler(CommandHandler("استعلامالرصيد", handle_address))
    app.add_handler(CommandHandler("تحققالمعاملات", handle_address))
    app.add_handler(CommandHandler("showbalance", handle_address))
    app.add_handler(CommandHandler("showtransactions", handle_address))
    app.add_handler(CommandHandler("عرضالبيانات", handle_address))
    app.add_handler(CommandHandler("walletquery", handle_address))
    app.add_handler(CommandHandler("querywallet", handle_address))
    app.add_handler(CommandHandler("walletcheckbsc", handle_address))
    app.add_handler(CommandHandler("txcheck", handle_address))
    app.add_handler(CommandHandler("query", handle_address))
    app.add_handler(CommandHandler("balancequery", handle_address))
    app.add_handler(CommandHandler("txquery", handle_address))
    app.add_handler(CommandHandler("checktx", handle_address))
    app.add_handler(CommandHandler("wallettx", handle_address))
    app.add_handler(CommandHandler("txwallet", handle_address))
    app.add_handler(CommandHandler("استعلاممحفظه", handle_address))

    app.run_polling()
