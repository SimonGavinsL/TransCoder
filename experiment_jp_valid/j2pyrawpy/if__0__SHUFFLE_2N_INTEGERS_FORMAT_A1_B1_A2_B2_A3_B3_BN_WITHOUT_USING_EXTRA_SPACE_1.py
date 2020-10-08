#!/usr/bin/env python
""" generated source for module if__0__SHUFFLE_2N_INTEGERS_FORMAT_A1_B1_A2_B2_A3_B3_BN_WITHOUT_USING_EXTRA_SPACE_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def shufleArray(cls, a, f, l):
        """ generated source for method shufleArray """
        if l - f == 1:
            return
        mid = (f + l) / 2
        temp = mid + 1
        mmid = (f + mid) / 2
        cls.shufleArray(a, f, mid)
        cls.shufleArray(a, mid + 1, l)

