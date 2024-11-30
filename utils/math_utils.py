class MathUtils:

  @staticmethod
  def normalize_dict(dictionary: dict):
    total_sum = sum(dictionary.values())
    percentage_dict = {key: round((value / total_sum) * 100, 2) for key, value in dictionary.items()}
    return dict(sorted(percentage_dict.items(), key=lambda item: item[1], reverse=True))
