import openai
from pyrogram import Client, filters
from EsproChat import EsproChat

# 🔑 API Credentials (Apne keys replace karo)
OPENAI_API_KEY = "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"  # OpenAI API key
# 🎯 OpenAI API Setup
openai.api_key = OPENAI_API_KEY

# 🤖 Memory System (User ke messages store karne ke liye)
user_memory = {}

# 🤖 AI-Based Chatbot with Context & Emojis
@EsproChat.on_message(filters.text & filters.private)
async def chat_with_ai(client, message):
    user_id = message.from_user.id
    user_input = message.text

    # 🧠 Pehle ki conversation yaad rakhne ke liye
    if user_id not in user_memory:
        user_memory[user_id] = []

    user_memory[user_id].append({"role": "user", "content": user_input})  # ✅ Corrected

    # 📡 OpenAI se response lo
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=user_memory[user_id] + [{"role": "system", "content": "Reply naturally with emojis"}]
    )

    ai_reply = response["choices"][0]["message"]["content"]

    # 🧠 Bot ka reply memory me store karo
    user_memory[user_id].append({"role": "assistant", "content": ai_reply})  # ✅ Corrected

    
