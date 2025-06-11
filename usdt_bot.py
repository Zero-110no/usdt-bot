import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

BSC_API_KEY = os.getenv("BSC_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أرسل عنوان محفظتك (BSC BEP-20)")

async def handle_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    address = update.message.text
    usdt_balance = get_usdt_balance(address)
    last_txns = get_last_transactions(address)
    msg = f"📦 الرصيد: {usdt_balance} USDT

🧾 آخر 10 معاملات:
" + "
".join(last_txns)
    await update.message.reply_text(msg)

def get_usdt_balance(address):
    url = f"https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=0x55d398326f99059fF775485246999027B3197955&address={address}&tag=latest&apikey={BSC_API_KEY}"
    res = requests.get(url).json()
    balance = int(res["result"]) / 1e18
    return round(balance, 4)

def get_last_transactions(address):
    url = f"https://api.bscscan.com/api?module=account&action=tokentx&contractaddress=0x55d398326f99059fF775485246999027B3197955&address={address}&sort=desc&apikey={BSC_API_KEY}"
    res = requests.get(url).json()
    txns = res.get("result", [])[:10]
    tx_list = []
    for tx in txns:
        direction = "⬆️ إرسال" if tx["from"].lower() == address.lower() else "⬇️ استلام"
        amount = int(tx["value"]) / 1e18
        tx_list.append(f"{direction}: {round(amount, 2)} USDT")
    return tx_list

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_address))
    app.run_polling()
