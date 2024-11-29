import sys


class ProgressLogger:

  @staticmethod
  def show_progress(percentage):
    sys.stdout.write(f"\rProgress: {percentage:.2f}%")
    sys.stdout.flush()
