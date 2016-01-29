from re import match
import csv

class SCCPRefcount(object):
  def __init__(self, data):
    self.__refs = list()
    self.__parse_refs(data)
    self.index = self.size()

  def __iter__(self):
    return self

  def __parse_refs(self, data):
    for line in data.split('\n'):
      if match(r'^\|\s+((\[\s*\d+\s*\])|(\+->))', line) is None:
        continue
      type, id = [ item.strip() for item in line.split('|')[2:4] ]
      if match(r'SEP[^/]+/.+', id) is None:
          dev, line = id, ""
      else:
          dev, line = id.split("/")
      self.__refs.append({"type": type, "dev": dev, "line": line})

  def size(self):
    return len(self.__refs)

  def device_exists(self, dev):
    return dev in [item['dev'] for item in self.__refs]

  def line_exists(self, line):
    return line in [item['line'] for item in self.__refs]

  def sub(self, channels):
    refs = list()
    for item in self.__refs:
      if channels.device_exists(item['dev']) is False:
        refs.append(item)
    self.__refs = refs
    self.index = self.size()

  def diff_csv(self, data):
    refs = list()
    for item in self.__refs:
      if self.in_list(item['dev'], data) is False:
        refs.append(item)
    return refs

  def in_list(self, data):
    for item in data:
      if self.device_exists(item['dev']):
        return True
    return False

  def next(self):
    if self.index == 0:
      raise StopIteration
    self.index = self.index - 1
    return self.__refs[self.index]

