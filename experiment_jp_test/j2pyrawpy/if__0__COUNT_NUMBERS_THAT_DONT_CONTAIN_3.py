#!/usr/bin/env python
""" generated source for module if__0__COUNT_NUMBERS_THAT_DONT_CONTAIN_3 """
class X(object):
    """ generated source for class X """
    @classmethod
    def count(cls, n):
        """ generated source for method count """
        if n >= 3 and n < 10:
            return n - 1
        po = 1
        while n / po > 9:
        msd = n / po
        if msd != 3:
            return cls.count(msd) * cls.count(po - 1) + cls.count(msd) + cls.count(n % po)
        else:
            return cls.count(msd * po - 1)

