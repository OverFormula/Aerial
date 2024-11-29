import time


def meta_collector(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    duration = end_time - start_time
    print(f"\n\n{func.__name__} executed in {duration:.2f} seconds")
    return result

  return wrapper
