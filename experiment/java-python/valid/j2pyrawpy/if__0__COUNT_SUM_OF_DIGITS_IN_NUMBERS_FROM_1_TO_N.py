#!/usr/bin/env python
""" generated source for module if__0__COUNT_SUM_OF_DIGITS_IN_NUMBERS_FROM_1_TO_N """
class X(object):
    """ generated source for class X """
    @classmethod
    def sumOfDigitsFrom1ToN(cls, n):
        """ generated source for method sumOfDigitsFrom1ToN """
        d = ((Math.log10(n)))
        a = [None]*d + 1
        a[0] = 0
        a[1] = 45
        p = ((Math.ceil(Math.pow(10, d))))
        msd = n / p
        return (msd * a[d] + (msd * (msd - 1) / 2) * p + msd * (1 + n % p) + cls.sumOfDigitsFrom1ToN(n % p))

