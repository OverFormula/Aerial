import asyncio

from config.aerial_config import AerialConfig
from telegram import Bot


class Messenger:
  config = AerialConfig()

  def send(self, message):
    telegram_token = self.config.get_telegram_token()
    bot = Bot(token=telegram_token)

    asyncio.run(bot.send_message(
      chat_id=self.config.get_chat(),
      text=message
    ))
