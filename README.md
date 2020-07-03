# filmy_bot
Данный бот принимает ссылку на фильм от пользователя, парсит контент и постит в канал.

python <= 3.7.0

# Install
```
git clone https://github.com/Doka-hub/filmy_bot.git
pip install -r requitements.txt
```
- ## Linux ( create .env )
  ```
  touch .env
  ```
- ## Windows ( create .env )
  ```
  copy con .env
  CTRL-Z
  ```
  ### .env
  ```
  api_id=TELEGRAM_API_ID
  api_hash=TELEGRAM_API_HASH
  bot_token=BOT_TOKEN
  username=USERNAME
  channel=CHANNEL
  ```
# RUN
```python bot.py```
