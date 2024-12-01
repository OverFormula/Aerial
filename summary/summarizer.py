from datetime import datetime

from config.aerial_config import AerialConfig
from git_data_accumulator import GitDataAccumulator
from measurement.progress import ProgressLogger
from measurement.timeless import meta_collector
from messaging.messenger import Messenger
from network.git_client import GitClient
from summary.message_builder import MessageBuilder


class Summarizer:
  config = AerialConfig()
  git_client = GitClient()
  messenger = Messenger()

  def summarize(self):
    data_accumulator = self.create_summary()
    self.send_summary(data_accumulator)

  @meta_collector
  def create_summary(self) -> GitDataAccumulator:
    print('Start summarizing with the config ' + self.config.config_path)
    data_accumulator = GitDataAccumulator(self.config)

    for repo in self.config.get_repositories():
      print(f'\nAnalyzing repository {repo}...')
      commits = self.get_commits(repo)
      self.analyze_commits(commits, repo, data_accumulator)

    return data_accumulator

  def get_commits(self, repo):
    now = datetime.now()
    first_day_of_month = datetime(now.year, now.month, 1).isoformat()

    return self.git_client.get_commits(repo, first_day_of_month)

  def analyze_commits(self, commits, repo: str, data_accumulator: GitDataAccumulator):
    for index, commit in enumerate(commits):
      commit_data = self.git_client.get_commit_data(commit)

      if commit_data['author']['login'] != self.config.get_author():
        continue

      data_accumulator.update(commit_data, repo)
      ProgressLogger.show_progress(index / len(commits) * 100)

    ProgressLogger.show_progress(100)

  def send_summary(self, data_accumulator: GitDataAccumulator):
    message = MessageBuilder.build_message(data_accumulator)
    print('\n' + message.caption)
    response = input('\n\nDo you want to send this to chat?\n').strip().lower()

    if response in ['yes', 'y']:
      self.messenger.send(message)
      print('\nmessage successfully sent to chat')


def main():
  summarizer = Summarizer()
  summarizer.summarize()


if __name__ == '__main__':
  main()
