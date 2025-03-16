import google.generativeai as genai
from pyrogram import Client, filters
from EsproChat import EsproChat  # Ensure EsproChat bot sahi setup hai

# 🎯 Google Gemini API Key Setup
GEMINI_API_KEY = "AIzaSyA180PDzcBt245Nqc5oBhldLMS3p3VrXPA"
genai.configure(api_key=GEMINI_API_KEY)

# 🤖 Memory System (User ke messages store karne ke liye)
user_memory = {}

# 🤖 AI-Based Chatbot (Sabhi Users ke liye)
@EsproChat.on_message(filters.text & filters.private)
async def chat_with_users(client, message):
    user_id = message.from_user.id
    user_input = message.text.strip()

    # 🧠 Pehle ki conversation yaad rakhne ke liye
    if user_id not in user_memory:
        user_memory[user_id] = []

    user_memory[user_id].append({"role": "user", "content": user_input})

    try:
        # ✅ Sahi API Version aur Method ka Use Karein
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content([user_input])  # Corrected method call

        ai_reply = response.text  # Gemini API ka response extract karna

        # 🧠 Bot ka reply memory me store karo
        user_memory[user_id].append({"role": "assistant", "content": ai_reply})

        # 🔄 User ko reply bhejo
        await message.reply_text(ai_reply)

    except Exception as e:
        await message.reply_text(f"❌ AI se reply lene me error aaya: {str(e)}")
