#!/usr/bin/env python
""" generated source for module if__1__DIVISIBILITY_BY_7 """
class X(object):
    """ generated source for class X """
    @classmethod
    def isDivisibleBy7(cls, num):
        """ generated source for method isDivisibleBy7 """
        if num < 10:
            return False
        return cls.isDivisibleBy7(num / 10 - 2 * (num - num / 10 * 10))

