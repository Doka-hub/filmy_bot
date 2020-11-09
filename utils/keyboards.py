from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton


def get_inline_keyboard(url: str) -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('🎥 Смотреть онлайн!', url=url),
                InlineKeyboardButton('🔎 Поиск фильмов!', url='some_url')
            ]
        ]
    )
    return inline_keyboard
