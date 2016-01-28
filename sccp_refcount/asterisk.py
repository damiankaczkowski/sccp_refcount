#from asterisk import manager

import asterisk.manager
import sys

manager = asterisk.manager.Manager()


class Asterisk(object):

    def __init__(self, username=username, password=password, host=host):
        self.__ami = manager.Manager()
        self.__ami.connect(host)
        self.__ami.login(username, password)

    def __del__(self):
        self.__ami.close()

    def is_connected(self):
        return self.__ami.connected()

