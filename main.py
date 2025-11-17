import os

import dotenv

from telegram import Client

dotenv.load_dotenv()

bot = Client()

@bot.event("on_message")
async def on_message(message):
    print(message.text)
    await bot.send(message.chat_id, "Hi!")

bot.run(os.environ['TOKEN'])