import telebot
from telebot import apihelper
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

# 1. CONFIGURATION
BOT_TOKEN = "8197292232:AAGFbLX2C_46Suopejnn71JHKVcTvG2sv1U"
ADMIN_ID = 8037979591
ADMIN_LINK = "https://t.me/nabil_the_ethical_hacker1"

# PythonAnywhere Free Account Proxy Configuration
apihelper.proxy = {'https': 'http://proxy.server:3128'}

# Connection Timeout adjustments for stability
apihelper.CONNECT_TIMEOUT = 30
apihelper.READ_TIMEOUT = 30

bot = telebot.TeleBot(BOT_TOKEN)

# 7. STABILITY (Remove webhook before starting)
try:
    print("Removing old webhooks to clear active sessions...")
    bot.remove_webhook()
    time.sleep(1)
except Exception as e:
    print(f"Webhook removal note: {e}")

# 3. NOTIFICATION SYSTEM Helper Function
def notify_admin_activity(user, action_details):
    try:
        username = f"@{user.username}" if user.username else "No Username"
        admin_message = (
            "🔔 **Bot Activity Alert!**\n\n"
            f"👤 **User:** {user.first_name} {user.last_name or ''}\n"
            f"🆔 **ID:** `{user.id}`\n"
            f"🏷️ **Username:** {username}\n"
            f"⚡ **Action:** {action_details}"
        )
        bot.send_message(ADMIN_ID, admin_message, parse_mode="Markdown")
    except Exception as e:
        print(f"Admin notification failed: {e}")

# 4. MAIN MENU GENERATOR
def get_main_menu():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🫡 Mobile Hacking RAT", callback_data="cat_mobile"))
    markup.row(InlineKeyboardButton("💻 Computer Hacking RAT", callback_data="cat_computer"))
    markup.row(InlineKeyboardButton("📂 Source Code", callback_data="cat_source"))
    markup.row(InlineKeyboardButton("🚀 APK FUD", callback_data="cat_apoo"))
    return markup


# --- 2. TWO-WAY FORWARDING & REPLY SYSTEM ---

@bot.message_handler(func=lambda message: True, content_types=['text', 'photo'])
def handle_messages(message):
    # Admin Reply System Logic
    if message.chat.id == ADMIN_ID and message.reply_to_message:
        try:
            # Check text or caption for target ID identification
            reply_text = message.reply_to_message.text or message.reply_to_message.caption
            if reply_text and "From User ID:" in reply_text:
                target_user_id = int(reply_text.split("From User ID:")[1].split("\n")[0].strip())
                
                if message.content_type == 'text':
                    bot.send_message(target_user_id, f"👨‍💻 **Admin Reply:** {message.text}")
                elif message.content_type == 'photo':
                    bot.send_photo(target_user_id, message.photo[-1].file_id, caption=message.caption)
                
                bot.send_message(ADMIN_ID, "✅ Reply sent successfully to the customer.")
            else:
                bot.send_message(ADMIN_ID, "❌ Please reply directly to a message containing 'From User ID:'.")
        except Exception as e:
            bot.send_message(ADMIN_ID, f"❌ Delivery Error: {str(e)}")
        return

    # User Logic
    if message.text == "/start":
        notify_admin_activity(message.from_user, "Started the bot (/start)")
        bot.send_message(
            message.chat.id, 
            "Welcome to our Dark World! Please select a category below:", 
            reply_markup=get_main_menu()
        )
    else:
        # Forward User messages to Admin with exact identification string
        username = f"@{message.from_user.username}" if message.from_user.username else "No Username"
        
        if message.content_type == 'text':
            log_msg = (
                f"📩 **New Message from Customer**\n"
                f"👤 Name: {message.from_user.first_name}\n"
                f"🏷️ Username: {username}\n"
                f"From User ID: {message.chat.id}\n\n"
                f"📝 Text: {message.text}"
            )
            bot.send_message(ADMIN_ID, log_msg)
            
        elif message.content_type == 'photo':
            caption_text = (
                f"📸 **New Screenshot Received!**\n"
                f"👤 Name: {message.from_user.first_name}\n"
                f"🏷️ Username: {username}\n"
                f"From User ID: {message.chat.id}\n"
            )
            if message.caption:
                caption_text += f"\n💬 User Caption: {message.caption}"
                
            bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption=caption_text)


# --- 5. CATEGORY DETAILS & 6. PAYMENT SCREEN ---

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    user = call.from_user

    if call.data == "main_menu":
        bot.edit_message_text("Welcome to our Dark World! Please select a category below:", chat_id, message_id, reply_markup=get_main_menu())
        return

    # Mobile io Category
    if call.data == "cat_mobile":
        notify_admin_activity(user, "Opened 'Mobile io' menu")
        text = "🫡 **Mobile Hacking RAT**\n\nPrice: **$30 each**\nSelect an option below to buy:"
        markup = InlineKeyboardMarkup()
        mobile_products = ["Craxs RAT, v6.8", "Craxs RAT, v7.3", "Craxs RAT, v7.4", "Craxs RAT, v7.6", "Craxs RAT, v7.7", "Craxs RAT, v8", "Eagle SPY, v3", "Eagle SPY, v4", "Eagle SPY, v5", "Eagle SPY, v6", "Cypher RAT, v3.6", "GTX_700 RAT, v7", "G-700 v6.2", "SPYNOTE, v7.2", "SPYNOTE, v7.3"]
        for p in mobile_products:
            markup.row(InlineKeyboardButton(f" {p} - $30", callback_data=f"prod_{p}_30"))
        markup.row(InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu"))
        bot.edit_message_text(text, chat_id, message_id, reply_markup=markup, parse_mode="Markdown")

    # Computer war Category
    elif call.data == "cat_computer":
        notify_admin_activity(user, "Opened 'Computer war' menu")
        text = "💻 **Computer Hacking RAT**\n\nPrice: **$80 each**\nSelect an option below to buy:"
        markup = InlineKeyboardMarkup()
        comp_products = ["Xworm v6", "Xworm v6.5", "Xworm v7.2", "Xworm v7.4", "Venom RAT v6.0.3", "888 RAT"]
        for p in comp_products:
            markup.row(InlineKeyboardButton(f" {p} - $80", callback_data=f"prod_{p}_80"))
        markup.row(InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu"))
        bot.edit_message_text(text, chat_id, message_id, reply_markup=markup, parse_mode="Markdown")

    # Source Code Category
    elif call.data == "cat_source":
        notify_admin_activity(user, "Opened 'Source Code' menu")
        text = "📂 **Source Code**\n\nPrice: **$100 each**\nSelect an option below to buy:"
        markup = InlineKeyboardMarkup()
        source_products = ["BTMOB v3.6 Source", "BTMOB v3.6.3 Source", "BTMOB v4 Source", "BTMOB v4.2 Source", "BTMOB v4.5.5 Source", "BTMOB v4.5.7 Source", "Craxs RAT V7.6 Source", "Eagle Spy v5 Source"]
        for p in source_products:
            markup.row(InlineKeyboardButton(f" {p} - $100", callback_data=f"prod_{p.replace(' ', '')}_100"))
        markup.row(InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu"))
        bot.edit_message_text(text, chat_id, message_id, reply_markup=markup, parse_mode="Markdown")

    # Apoo lo Category
    elif call.data == "cat_apoo":
        notify_admin_activity(user, "Opened 'Apoo lo' menu")
        text = "🚀 **APK FUD**\n\nPrice: **$100**\nSelect options below:"
        markup = InlineKeyboardMarkup()
        markup.row(InlineKeyboardButton("💳 Pay Now ($100)", callback_data="prod_Apoolo_100"))
        markup.row(InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu"))
        bot.edit_message_text(text, chat_id, message_id, reply_markup=markup, parse_mode="Markdown")

    # Payment details screen logic
    elif call.data.startswith("prod_"):
        parts = call.data.split("_")
        prod_name = parts[1]
        amount = parts[2]
        
        notify_admin_activity(user, f"Selected Item: {prod_name} (${amount}) - Viewing payment details")
        
        text = (
            f"💳 **Payment Details**\n\n"
            f"Product Selected: **{prod_name}**\n"
            f"Total Amount: **${amount}**\n\n"
            "Please copy the address below by tapping on it:\n\n"
            "🪙 **USDT (TRC20):**\n`THh9CXPcb465cA3rSfBZYqj4gYSkk7YLCR`\n\n"
            "🪙 **Bitcoin (BTC):**\n`15JTcfh3CkW1X6rd5U1EVdmxe8h2k97iaE`\n\n"
            f"⚠️ **Important:** After completing the payment, please send the transaction screenshot directly here in this chat. "
            "The admin will verify and approve your order shortly."
        )
        markup = InlineKeyboardMarkup()
        markup.row(InlineKeyboardButton("🔙 Back to Main Menu", callback_data="main_menu"))
        bot.edit_message_text(text, chat_id, message_id, reply_markup=markup, parse_mode="Markdown", disable_web_page_preview=True)

    try:
        bot.answer_callback_query(call.id)
    except Exception:
        pass


# 7. STABILITY (Start Polling loop tailored for network conditions)
if __name__ == "__main__":
    print("Bot initialization complete...")
    while True:
        try:
            bot.polling(none_stop=True, timeout=60)
        except Exception as e:
            print(f"Network status alert: {e}. Re-attempting connection in 5 seconds...")
            time.sleep(5)