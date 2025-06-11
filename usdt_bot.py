import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TELEGRAM_TOKEN = "توكن_البوت_بتاعك"
BSCSCAN_API_KEY = "مفتاح_BSCScan_بتاعك"

def get_usdt_balance(address):
    url = f"https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=0x55d398326f99059fF775485246999027B3197955&address={address}&tag=latest&apikey={BSCSCAN_API_KEY}"
    response = requests.get(url)
    data = response.json()
    balance = int(data["result"]) / 10**18
    return round(balance, 2)

def get_transactions(address):
    url = f"https://api.bscscan.com/api?module=account&action=tokentx&address={address}&contractaddress=0x55d398326f99059fF775485246999027B3197955&page=1&offset=10&sort=desc&apikey={BSCSCAN_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("result", [])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أرسل عنوان محفظتك عشان أجيب ليك الرصيد والمعاملات.")

async def handle_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    address = update.message.text.strip()
    if address.startswith("0x") and len(address) == 42:
        try:
            usdt_balance = get_usdt_balance(address)
            txs = get_transactions(address)
            msg = f"الرصيد: {usdt_balance} USDT\n\nآخر 10 معاملات:\n"
            for tx in txs:
                from_addr = tx["from"]
                to_addr = tx["to"]
                amount = int(tx["value"]) / 10**18
                msg += f"- {amount:.2f} USDT من {from_addr[:6]}... إلى {to_addr[:6]}...\n"
            await update.message.reply_text(msg)
        except:
            await update.message.reply_text("حصل خطأ، حاول تاني.")
    else:
        await update.message.reply_text("العنوان ما صحيح.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("check", handle_address))
    app.add_handler(CommandHandler("balance", handle_address))
    app.add_handler(CommandHandler("tx", handle_address))
    app.run_polling()
