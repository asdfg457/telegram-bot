import os
import telebot
from telebot import types

# التوكن يقرأ من Environment Variable في Render
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# ID مالك البوت (غيره وحط الـ id مالك)
OWNER_ID = 6366726970

# استقبال أي رسالة
@bot.message_handler(func=lambda message: True)
def send_user_info(message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name

    info = f"👤 مستخدم جديد:\n"
    info += f"🆔 ID: {user_id}\n"
    info += f"🔗 Username: @{username}\n" if username else "🔗 لا يوجد يوزر\n"
    info += f"📛 الاسم: {first_name}"

    # يرسل المعلومات إليك
    bot.send_message(OWNER_ID, info)

    # يطلب من المستخدم مشاركة رقم الهاتف
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button = types.KeyboardButton("📱 مشاركة الرقم", request_contact=True)
    markup.add(button)
    bot.reply_to(message, "✅ تم تسجيلك.\nالرجاء مشاركة رقم هاتفك:", reply_markup=markup)

# استقبال الرقم من المستخدم
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    if message.contact is not None:
        phone = message.contact.phone_number
        user_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name

        info = f"📱 رقم هاتف مستخدم جديد:\n"
        info += f"🆔 ID: {user_id}\n"
        info += f"🔗 Username: @{username}\n" if username else "🔗 لا يوجد يوزر\n"
        info += f"📛 الاسم: {first_name}\n"
        info += f"📞 الهاتف: {phone}"

        # إرسال الرقم إلى مالك البوت
        bot.send_message(OWNER_ID, info)

        bot.send_message(message.chat.id, "✅ تم استلام رقم هاتفك بنجاح!")

print("🚀 البوت يعمل...")
bot.polling()
