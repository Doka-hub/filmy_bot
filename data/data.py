from typing import Union
from decouple import config


API_ID: str = config('API_ID')
API_HASH: str = config('API_HASH')
BOT_TOKEN: str = config('BOT_TOKEN')
ADMIN: Union[int, str] = config('ADMIN')
CHANNEL_ID: Union[int, str] = config('CHANNEL_ID')

