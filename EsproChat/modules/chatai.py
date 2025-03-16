import google.generativeai as genai
from pyrogram import Client, filters
from EsproChat import EsproChat  # Ensure EsproChat bot sahi setup hai

# 🎯 Google Gemini API Key Setup
GEMINI_API_KEY = "your_google_gemini_api_key"
genai.configure(api_key=GEMINI_API_KEY)

# 🤖 Memory System (User ke messages store karne ke liye)
user_memory = {}

# 🤖 AI-Based Chatbot with Context (Sirf "Kaal" ke liye)
@EsproChat.on_message(filters.text & filters.private)
async def chat_with_kaal(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name  # Sender ka naam
    user_input = message.text.strip()

    # ✅ Check karein ki user ka naam "Kaal" hai ya nahi
    if user_name.lower() != "kaal":
        return  # Agar naam "Kaal" nahi hai toh bot reply nahi karega

    # 🧠 Pehle ki conversation yaad rakhne ke liye
    if user_id not in user_memory:
        user_memory[user_id] = []

    user_memory[user_id].append({"role": "user", "content": user_input})

    try:
        # 📡 Gemini AI se response lo
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)

        ai_reply = response.text  # Gemini API ka response extract karna

        # 🧠 Bot ka reply memory me store karo
        user_memory[user_id].append({"role": "assistant", "content": ai_reply})

      

    except Exception as e:
        await message.reply_text("❌ AI se reply lene me error aaya: " + str(e))
