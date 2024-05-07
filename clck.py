class Clock:
  def __init__(self, tm, tmzone):
    self.tm = tm;
    self.tmzone = tmzone;

  def calculateHeximalTime(self):
    secs = round(self.tm % 60);
    mins = round(self.tm % 3600 // 60);
    hrs = round((self.tm % 86400 // 3600 + self.tmzone) % 24);
    return hrs, mins, secs, "", "";

  def calculateDecimalTime(self):
    secs = round(self.tm % 100);
    mins = round(self.tm % 10000 // 100);
    hrs = round(self.tm % 1000000 // 10000);
    days = round(self.tm % 10000000 // 1000000);
    mths = round(self.tm % 100000000 // 10000000);
    return hrs, mins, secs, mths, days;

