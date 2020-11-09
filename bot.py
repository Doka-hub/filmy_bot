from pyrogram import Client, Filters
from pyrogram.client.types import Message

from utils import parsing, get_inline_keyboard

from data import API_ID, API_HASH, BOT_TOKEN, ADMIN, CHANNEL_ID


bot = Client('example', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@bot.on_message(Filters.regex('http') & Filters.user == ADMIN)
def post(client: Client, message: Message) -> None:
    url = message.text
    text, url = parsing(url)
    inline_keyboard = get_inline_keyboard(url)

    client.send_message(CHANNEL_ID, text, reply_markup=inline_keyboard)


bot.run()
