import os

import dotenv

import telegram

dotenv.load_dotenv()

bot = telegram.Client()

@bot.event("on_message")
async def on_message(message: telegram.Message):
    text = message.text.lower()

    replies: dict[tuple, str] = {
    ('hi', 'hello', 'hey'): f'{text.capitalize()} {message.author.first_name}!, How are you.',
    ('gm', 'good morning'): f'Good Morning {message.author.first_name}, have a great day ahead <3',
    ('gn', 'good night'): f'Good Night {message.author.first_name}, have sweet dreams :)'
}

    for triggers in replies:
        if text in triggers:
            await bot.send(message.chat_id, replies[triggers])
    

bot.run(os.environ['TOKEN'])