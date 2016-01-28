from nose.tools import *
from sccp_refcount.sccprefcount import SCCPRefcount
from sccp_refcount.sccpchans import SCCPChans

class TestSCCPRefcountClass(object):
    def setUp(self):
        self.filename = "tests/refcount.out"
        self.refs = SCCPRefcount(self.filename)

    def test_count_parsed_refs(self):
        r = self.refs
        assert_equal(r.size(), 1497)

    def test_iterate_refs(self):
        r = self.refs
        for ref in r:
            assert_true(isinstance(ref, dict))

    def test_device_exists(self):
        r = self.refs
        assert_true(r.device_exists("SEP00190670D78D"))

    def test_device_not_exist(self):
        r = self.refs
        assert_false(r.device_exists("SEP000000000000"))

    def test_line_exists(self):
        r = self.refs
        assert_true(r.line_exists("3026"))

    def test_line_not_exists(self):
        r = self.refs
        assert_false(r.line_exists("000000"))

    def test_refs_sub_channels(self):
        r = self.refs
        chans = SCCPChans("tests/sccpchans.out")
        assert_true(r.device_exists("SEP00192F7F272F"))
        r.sub(chans)
        assert_false(r.device_exists("SEP00192F7F272F"))
        assert_equal(r.size(), 1451)


