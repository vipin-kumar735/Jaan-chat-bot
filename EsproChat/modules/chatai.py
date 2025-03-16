import openai
from pyrogram import Client, filters
from EsproChat import EsproChat

# 🎯 OpenAI API Setup
OPENAI_API_KEY = "your_openai_api_key"  # Apni OpenAI API Key yahan dalein
openai.api_key = OPENAI_API_KEY

# 🤖 Memory System (User ke messages store karne ke liye)
user_memory = {}

# 🤖 AI-Based Chatbot with Context
@EsproChat.on_message(filters.text & filters.private)
async def chat_with_ai(client, message):
    user_id = message.from_user.id
    user_input = message.text.strip()  # Extra spaces hatane ke liye

    # 🧠 Pehle ki conversation yaad rakhne ke liye
    if user_id not in user_memory:
        user_memory[user_id] = [
            {"role": "system", "content": "You are a friendly AI assistant. Reply naturally with emojis!"}
        ]

    # User ka message memory me add karein
    user_memory[user_id].append({"role": "user", "content": user_input})

    try:
        # 📡 OpenAI se response lo (Latest API Syntax)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=user_memory[user_id],  # Poori conversation bhej rahe hain
            temperature=0.7  # Creativity ka level (0.0 = Bilkul strict, 1.0 = Zyada creative)
        )

        ai_reply = response["choices"][0]["message"]["content"]  # ✅ Latest SDK ke hisaab se access karna

        # 🧠 Bot ka reply memory me store karo
        user_memory[user_id].append({"role": "assistant", "content": ai_reply})


    except openai.error.OpenAIError as e:
        await message.reply_text("❌ AI se reply lene me error aaya: " + str(e))
