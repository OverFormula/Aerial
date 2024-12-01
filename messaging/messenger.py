import asyncio

from config.aerial_config import AerialConfig
from telegram import Bot

from summary.complex_message import ComplexMessage


class Messenger:
  config = AerialConfig()

  def send(self, message: ComplexMessage):
    telegram_token = self.config.get_telegram_token()
    bot = Bot(token=telegram_token)

    asyncio.run(bot.send_photo(
      chat_id=self.config.get_chat(),
      photo=message.image,
      caption=message.caption,
    ))

    # asyncio.run(bot.send_message(
    #   chat_id=self.config.get_chat(),
    #   text=message,
    #   disable_web_page_preview=True
    # ))
