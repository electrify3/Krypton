import os

import dotenv

import telegram

dotenv.load_dotenv()

bot = telegram.Client()

@bot.event("on_message")
async def on_message(message: telegram.Message):
    text = message.text.lower()

    if text in ['hi', 'hi', 'hello', 'hey']:
        await bot.send(message.chat_id, f"{text.capitalize()} {message.author.first_name}!, How are you.")
    

bot.run(os.environ['TOKEN'])