from summary.git_data_accumulator import GitDataAccumulator


class MessageBuilder:

  @staticmethod
  def build_message(data_accumulator: GitDataAccumulator) -> str:
    message = "Github activity summary: " + "\n\n"

    for repo in data_accumulator.repositories:
      message = MessageBuilder.add_repository_info(repo, data_accumulator, message)

    message = MessageBuilder.add_general_info(data_accumulator, message)
    return message

  @staticmethod
  def add_repository_info(repo, data_accumulator: GitDataAccumulator, message) -> str:
    if data_accumulator.unchanged(repo):
      return message

    message += "github.com/" + repo + " summary: " + "\n"

    message += "Commits count: " + str(data_accumulator.project_to_commits_count[repo]) + "\n"
    message += "Files changed: " + str(data_accumulator.project_to_files_changed[repo])
    message += " (+" + str(data_accumulator.project_to_additions[repo])
    message += " -" + str(data_accumulator.project_to_deletions[repo]) + ")" + "\n\n"

    return message

  @staticmethod
  def add_general_info(data_accumulator: GitDataAccumulator, message) -> str:
    message += "Number of days with commits: " + str(len(data_accumulator.dates)) + "\n"

    if len(data_accumulator.locations) > 1:
      locations = '\n '.join(map(str, data_accumulator.locations))
      message += 'Commit locations: ' + '\n ' + locations + '\n\n'
    else:
      locations = (str(data_accumulator.locations)
                   .replace("[", "")
                   .replace("]", "")
                   .replace("'", ""))
      message += "Commit locations: " + locations

    return message
