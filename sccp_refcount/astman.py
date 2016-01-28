from asterisk import manager

class Astman(object):

    def __init__(self, username, password, host):
        self.__ami = manager.Manager()
        self.__ami.connect(host)
        self.__ami.login(username, password)

    def __del__(self):
        self.__ami.close()

    def is_connected(self):
        return self.__ami.connected()

    def sccp_channels(self):
        res = self.__ami.command('sccp show channels')
        return res.data

    def sccp_refcount(self):
        res = self.__ami.command('sccp show refcount')
        return res.data
