import json
import os
from typing import Any


class AerialConfig:
  config_data: Any
  manual_data: Any
  config_path: str

  def __init__(self):
    environment = os.getenv('ENV', 'Production')
    self.config_path = '../config/config_dev.json' if environment == 'development' else '../config/config.json'

    with open(self.config_path) as config:
      self.config_data = json.load(config)
    with open('../config/manual.json') as manual:
      self.manual_data = json.load(manual)

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

  def enable_manual(self):
    return self.manual_data['enable'] if self.manual_data else False

  def get_extra_days(self):
    return self.manual_data['extra_days']

  def get_manual_projects(self):
    return self.manual_data['projects']
