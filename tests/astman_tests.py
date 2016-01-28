from nose.tools import *
from sccp_refcount.asterisk import Asterisk

class TestAsteriskManagerClass(object):

  def test_connection(self):
    user = 'ets_usrmgm'
    pswd = 'aeL8Wuma6foh'
    host = '10.130.12.66'
    #man = Asterisk(username = user, password = pswd, host = host)
    #assert_true(man.is_connected())

