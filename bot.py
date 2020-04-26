from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton
import custom_utils
import os
from decouple import config


app2 = Client(
    'filmy_bot',
    api_id=config('api_id'),
    api_hash=config('api_hash'),
    bot_token=config('bot_token')
)


@app2.on_message(Filters.regex('http'))
def post(client, message):
    if message.chat.username == 'screlizer':
        url = message.text
        text = custom_utils.parsing(url)
        client.send_message(
            'filmy',
            text[0],
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton('🎥 Смотреть онлайн!', url=text[1]),
                InlineKeyboardButton('🔎 Поиск фильмов!', url='http://f1.ikino.site/index.php?do=search')
            ]]),
        )


app2.run()

