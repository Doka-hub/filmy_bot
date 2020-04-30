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
    if message.chat.username == 'some_name':
        url = message.text
        text = custom_utils.parsing(url)
        client.send_message(
            'filmy',
            text[0],
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton('🎥 Смотреть онлайн!', url=text[1]),
                InlineKeyboardButton('🔎 Поиск фильмов!', url='some_url')
            ]]),
        )
        client.send_message(
            'filmyserial',
            text[0],
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton('🎥 Смотреть онлайн!', url=text[1]),
                InlineKeyboardButton('🔎 Поиск фильмов!', url='some_url')
            ]]),
        )


app2.run()

