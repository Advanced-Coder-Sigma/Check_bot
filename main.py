import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.helpers import escape_markdown

BOT_TOKEN = "7311258512:AAHyNQX3QHsHAFh5uIx-ERsCVcK7_WIKwqM"
BOT_OWNER = "@Bhaiya_chips"
BOT_CREDITS = "@ItsMeCutehack"

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if len(context.args) != 1 or not context.args[0].isdigit():
            await update.message.reply_text(
                "❌ *Usage*: /check \\{uid\\}\n✅ *Example*: /check 123456789",
                parse_mode="MarkdownV2"
            )
            return

        uid = escape_markdown(context.args[0], version=2)
        api_url = f"https://amin-belara-api.vercel.app/check_banned?player_id={uid}"
        response = requests.get(api_url)
        response.raise_for_status()
        response_data = response.json()

        player_name = response_data.get("player_name", "Unknown")
        status = response_data.get("status", "Unknown")
        formatted_name = escape_markdown(player_name.replace("_", " "), version=2)

        account_status = "🟢 *Not Banned*" if status == "NOT BANNED" else "🔴 *Banned*"

        message = (
            f"👤 *Owner*: {escape_markdown(BOT_OWNER, version=2)}\n"
            f"🎮 *User*: {formatted_name}\n"
            f"📌 *UID*: {uid}\n"
            f"🛡️ *Status*: {account_status}\n"
            f"🔰 *Credits*: {escape_markdown(BOT_CREDITS, version=2)}"
        )
        await update.message.reply_text(message, parse_mode="MarkdownV2")

    except requests.exceptions.RequestException as e:
        await update.message.reply_text(
            f"🚨 API Error: {escape_markdown(str(e), version=2)}",
            parse_mode="MarkdownV2"
        )
    except Exception as e:
        await update.message.reply_text(
            f"🚨 Unexpected Error: {escape_markdown(str(e), version=2)}",
            parse_mode="MarkdownV2"
        )

async def region(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if len(context.args) != 1 or not context.args[0].isdigit():
            await update.message.reply_text(
                "❌ *Usage*: /region \\{uid\\}\n✅ *Example*: /region 123456789",
                parse_mode="MarkdownV2"
            )
            return

        uid = escape_markdown(context.args[0], version=2)
        api_url = f"https://amin-belara-api.vercel.app/check_banned?player_id={uid}"
        response = requests.get(api_url)
        response.raise_for_status()
        response_data = response.json()

        player_name = response_data.get("player_name", "Unknown")
        region = response_data.get("region", "Unknown")
        formatted_name = escape_markdown(player_name.replace("_", " "), version=2)

        message = (
            f"👤 *Owner*: {escape_markdown(BOT_OWNER, version=2)}\n"
            f"🎮 *User*: {formatted_name}\n"
            f"📌 *UID*: {uid}\n"
            f"🌍 *Region*: {escape_markdown(region, version=2)}\n"
            f"🔰 *Credits*: {escape_markdown(BOT_CREDITS, version=2)}"
        )
        await update.message.reply_text(message, parse_mode="MarkdownV2")

    except requests.exceptions.RequestException as e:
        await update.message.reply_text(
            f"🚨 API Error: {escape_markdown(str(e), version=2)}",
            parse_mode="MarkdownV2"
        )
    except Exception as e:
        await update.message.reply_text(
            f"🚨 Unexpected Error: {escape_markdown(str(e), version=2)}",
            parse_mode="MarkdownV2"
        )

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("check", check))
    application.add_handler(CommandHandler("region", region))
    print("🚀 Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
