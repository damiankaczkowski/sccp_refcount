from re import match
from os import path

class SCCPRefcount(object):
  def __init__(self, filename):
    if not path.exists(filename):
      raise IOError("File %s not found" % filename)
    fd = open(filename, "r")
    self.__refs = list()
    self.__parse_refs(fd)
    self.index = self.size()

  def __iter__(self):
    return self

  def __parse_refs(self, fd):
    for line in fd:
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

  def next(self):
    if self.index == 0:
      raise StopIteration
    self.index = self.index - 1
    return self.__refs[self.index]

