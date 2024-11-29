import json
from typing import Any


class AerialConfig:
  config_data: Any

  def __init__(self):
    with open('../config/config.json') as config:
      self.config_data = json.load(config)

  def get_telegram_token(self):
    return self.config_data['telegram_token']

  def get_chat(self):
    return self.config_data['chat_id']

  def get_display_name(self):
    return self.config_data['display_name']

  def get_github_token(self):
    return self.config_data['github_token']

  def get_repositories(self):
    return self.config_data['repositories']

  def get_author(self):
    return self.config_data['author']

  def get_locations(self):
    return self.config_data['locations']
