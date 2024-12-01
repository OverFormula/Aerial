import matplotlib.pyplot as plt
import numpy as np
import calendar
from io import BytesIO

from datetime import datetime, timedelta


class Visualizer:

  @staticmethod
  def generate_monthly_heatmap(contributions):
    now = datetime.now()
    year = now.year
    month = now.month

    _, num_days = calendar.monthrange(year, month)

    start_date = datetime(year, month, 1)
    date_range = [start_date + timedelta(days=i) for i in range(num_days)]

    heatmap_data = np.zeros((7, 5))
    for date in date_range:
      week = (date.day - 1) // 7
      weekday = date.weekday()
      date_str = date.strftime('%Y-%m-%d')
      heatmap_data[weekday, week] = contributions.get(date_str, 0)

    plt.figure(figsize=(10, 7))
    plt.title(f'GitHub Activity Heatmap for {calendar.month_name[month]} {year}')
    plt.imshow(heatmap_data, cmap='Oranges', aspect='auto')
    plt.colorbar(label='Contributions')
    plt.yticks(range(7), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.xticks(range(5), [f'Week {i + 1}' for i in range(5)])

    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()
    image_stream.seek(0)

    return image_stream
