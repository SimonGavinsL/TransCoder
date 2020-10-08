#!/usr/bin/env python
""" generated source for module if__0__LAST_NON_ZERO_DIGIT_FACTORIAL """
class X(object):
    """ generated source for class X """
    @classmethod
    def lastNon0Digit(cls, n):
        """ generated source for method lastNon0Digit """
        if ((n / 10) % 10) % 2 == 0:
            return (6 * cls.lastNon0Digit(n / 5) * dig[n % 10]) % 10
        else:
            return (4 * cls.lastNon0Digit(n / 5) * dig[n % 10]) % 10

