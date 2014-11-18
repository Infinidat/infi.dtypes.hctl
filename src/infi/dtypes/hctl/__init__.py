__import__("pkg_resources").declare_namespace(__name__)

import sys
from collections import namedtuple

PY2 = sys.version_info[0] == 2
string_type = basestring if PY2 else str

class NamedTupleAddress(object):
    _TUPLE = None
    def __init__(self, *args, **kwargs):
        super(NamedTupleAddress, self).__init__()
        self._value = self._TUPLE(*args, **kwargs) #pylint: disable-msg=E1102
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._value == other._value
        if isinstance(other, string_type):
            return self == type(self).from_string(other)
        return False
    def __ne__(self, other):
        return not (self == other)
    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError()
        return self._value < other._value
    def __le__(self, other):
        return self == other or self < other
    def __gt__(self, other):
        return not (self <= other)
    def __ge__(self, other):
        return not self < other
    def __iter__(self):
        return iter(self._value)
    def __hash__(self):
        return hash(str(self))
    @classmethod
    def from_string(cls, s):
        if not isinstance(s, string_type):
            raise ValueError(s)
        return cls(*map(int, s.split(":")))
    def __repr__(self):
        return "<{0}>".format(self)
    def __str__(self):
        return ":".join(map(str, self._value))

class HCT(NamedTupleAddress):
    _TUPLE = namedtuple("HCT", tuple("hct"))
    def get_host(self):
        return self._value.h
    def get_channel(self):
        return self._value.c
    def get_target(self):
        return self._value.t
    def __getitem__(self, l):
        return HCTL(self._value.h, self._value.c, self._value.t, l)

class HCTL(HCT):
    _TUPLE = namedtuple("HCTL", tuple("hctl"))
    def get_lun(self):
        return self._value.l
    @classmethod
    def from_hct_and_lun(cls, hct, lun):
        return cls(hct.get_host(), hct.get_channel(), hct.get_target(), lun)

