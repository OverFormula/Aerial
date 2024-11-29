import requests

from config.aerial_config import AerialConfig


class GitClient:
  config = AerialConfig()

  def get_commits(self, repo, since):
    params = {'since': since}

    response = requests.get(
      f'https://api.github.com/repos/{repo}/commits',
      headers={'Authorization': f'token {self.config.get_github_token()}'},
      params=params
    )
    response.raise_for_status()
    return response.json()

  def get_commit_data(self, commit):
    commit_url = commit['url']
    response = requests.get(
      commit_url,
      headers={'Authorization': f'token {self.config.get_github_token()}'}
    )

    response.raise_for_status()
    return response.json()
