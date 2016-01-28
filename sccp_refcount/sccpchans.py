from re import match

class SCCPChans(object):
  def __init__(self, data):
    self.__channels = list()
    self.__parse_chans(data)
    self.index = self.size()

  def __iter__(self):
    return self

  def __parse_chans(self, data):
    for line in data.split('\n'):
      if match(r'^\|\s+\d+\s+', line) is None:
        continue
      name,line,dev = line.split()[2:5]
      self.__channels.append({"name": name, "line": line, "dev": dev})

  def device_exists(self, dev):
    return dev in [item['dev'] for item in self.__channels]

  def line_exists(self, line):
    return line in [item['line'] for item in self.__channels]

  def size(self):
    return len(self.__channels)

  def next(self):
    if self.index == 0:
      raise StopIteration
    self.index = self.index - 1
    return self.__channels[self.index]
