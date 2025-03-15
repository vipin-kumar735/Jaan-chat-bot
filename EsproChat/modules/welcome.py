from EsproChat import EsproChat as app
import random
from pyrogram import Client, filters

# Alag-alag welcome messages ka list
welcome_messages = [
    "Kese ho aap?",
    "Aap kaise ho?",
    "Mujhe aap se milke accha laga!",
    "Aap ka din shubh ho!",
    "Umeed hai aap maze me ho!",
    "Kaise chal raha hai sab?"
]

@app.on_message(filters.new_chat_members)
def welcome(client, message):
    for member in message.new_chat_members:
        username = member.username
        name = member.first_name
        if username:
            mention = f"[{name}](https://t.me/{username})"
        else:
            mention = name

        # Random message select karna
        random_message = random.choice(welcome_messages)

        welcome_text = f"{mention} Welcome Baby😁❤️\n{random_message}"
        message.reply_text(welcome_text, disable_web_page_preview=True)
