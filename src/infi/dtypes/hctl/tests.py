import unittest
from . import HCTL, HCT

subject = HCTL(1, 0, 0, 1)

class HCTLTestCase(unittest.TestCase):
    def test_getters(self):
        self.assertEqual(subject.get_host(), 1)
        self.assertEqual(subject.get_channel(), 0)
        self.assertEqual(subject.get_target(), 0)
        self.assertEqual(subject.get_lun(), 1)

    def test_fromstring(self):
        self.assertEqual(subject, HCTL.from_string("1:0:0:1"))
        self.assertNotEqual(subject, HCTL.from_string("1:0:0:2"))
        self.assertLessEqual(subject, HCTL.from_string("1:0:0:2"))

    def test_from_hct_and_lun(self):
        self.assertEqual(HCTL.from_hct_and_lun(HCT(1, 2, 3), 4), HCTL(1, 2, 3, 4))

    def test_opeators(self):
        self.assertEqual(subject, "1:0:0:1")
        self.assertFalse(subject == 123)
        self.assertRaises(TypeError, subject.__lt__, None)
        self.assertGreaterEqual(subject, HCTL.from_string("1:0:0:0"))
        self.assertGreater(subject, HCTL.from_string("1:0:0:0"))
        self.assertEqual([i for i in subject], [1, 0, 0, 1])
        self.assertRaises(ValueError, subject.from_string, None)
        self.assertEqual(repr(subject), "<1:0:0:1>")
        self.assertEqual(HCT(1, 0, 0)[1], subject)
