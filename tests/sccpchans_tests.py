from nose.tools import *
from sccp_refcount.sccpchans import SCCPChans

class TestSCCPChansClass(object):
    def setUp(self):
        self.fd = open("tests/sccpchans.out", "r")
        self.data = self.fd.read()
        self.channels = SCCPChans(self.data)

    def tearDown(self):
        self.fd.close()

    def test_device_exists(self):
        c = self.channels
        assert_true(c.device_exists("SEP00192F0C0FE3"))

    def test_device_not_exist(self):
        c = self.channels
        assert_false(c.device_exists("SEP000000000000"))

    def test_line_exists(self):
        c = self.channels
        assert_true(c.line_exists("3026"))

    def test_line_not_exists(self):
        c = self.channels
        assert_false(c.line_exists("000000"))

    def test_count_channels_parsed(self):
        c = self.channels
        assert_equal(c.size(), 26)

    def test_iterate_chans(self):
        c = self.channels
        for chan in c:
            assert_true(isinstance(chan, dict))

