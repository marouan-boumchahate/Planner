class TimeException(Exception):
  def __init__(self, message):
    super().__init__("\n" + message + "\n")
