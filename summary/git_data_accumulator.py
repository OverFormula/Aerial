from config.aerial_config import AerialConfig
from summary.language_analyzer import LanguageAnalyzer


def increment(dictionary: dict, key, value):
  if key in dictionary:
    dictionary[key] += value
  else:
    dictionary[key] = value


class GitDataAccumulator:

  def __init__(self, config: AerialConfig):
    self.project_to_files_changed = {}
    self.project_to_commits_count = {}
    self.project_to_additions = {}
    self.project_to_deletions = {}
    self.language_to_changes = {}
    self.contributions = {}
    self.dates = set()
    self.locations = config.get_locations()
    self.extra_days = config.get_extra_days() if (config.enable_manual() and config.get_extra_days()) else 0

    manual_projects_repositories = [project['repo'] for project in
                                    config.get_manual_projects()] if config.enable_manual() else []
    self.repositories = config.get_repositories() + manual_projects_repositories

    if config.enable_manual():
      manual_projects = config.get_manual_projects()
      for project in manual_projects:
        self.update_manual(project)

  def update(self, commit_data, repo: str):
    commit_stats = commit_data['stats']
    additions = commit_stats['additions']
    deletions = commit_stats['deletions']
    files_changed = len(commit_data.get('files', []))

    increment(self.project_to_commits_count, repo, 1)
    increment(self.project_to_files_changed, repo, files_changed)
    increment(self.project_to_additions, repo, additions)
    increment(self.project_to_deletions, repo, deletions)
    self.update_languages(commit_data)
    date = commit_data['commit']['committer']['date'][:10]
    self.dates.add(date)
    self.contributions[date] = self.contributions.get(date, 0) + 1

  def update_manual(self, project):
    repo = project['repo']
    increment(self.project_to_commits_count, repo, project['commits'])
    increment(self.project_to_additions, repo, project['additions'])
    increment(self.project_to_deletions, repo, project['deletions'])
    increment(self.project_to_files_changed, repo, project['files_changed'])

  def update_languages(self, commit_data):
    for file in commit_data['files']:
      language = LanguageAnalyzer.detect_language(file['filename'])
      increment(self.language_to_changes, language, file['changes'])

  def unchanged(self, repo: str):
    return repo not in self.project_to_files_changed
