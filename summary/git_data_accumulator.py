from config.aerial_config import AerialConfig


def increment(dictionary: dict, key, value):
  if key in dictionary:
    dictionary[key] += value
  else:
    dictionary[key] = value


class GitDataAccumulator:

  def __init__(self, config: AerialConfig):
    self.repositories = config.get_repositories()
    self.project_to_files_changed = {}
    self.project_to_commits_count = {}
    self.project_to_additions = {}
    self.project_to_deletions = {}
    self.dates = set()
    self.locations = config.get_locations()

  def update(self, commit_data, repo: str):
    commit_stats = commit_data['stats']
    additions = commit_stats['additions']
    deletions = commit_stats['deletions']
    files_changed = len(commit_data.get('files', []))

    increment(self.project_to_commits_count, repo, 1)
    increment(self.project_to_files_changed, repo, files_changed)
    increment(self.project_to_additions, repo, additions)
    increment(self.project_to_deletions, repo, deletions)
    self.dates.add(commit_data['commit']['committer']['date'][:10])

  def unchanged(self, repo: str):
    return repo not in self.project_to_files_changed
