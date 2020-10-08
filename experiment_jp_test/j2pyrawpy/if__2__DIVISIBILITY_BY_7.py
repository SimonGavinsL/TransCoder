#!/usr/bin/env python
""" generated source for module if__2__DIVISIBILITY_BY_7 """
class X(object):
    """ generated source for class X """
    @classmethod
    def isDivisibleBy7(cls, num):
        """ generated source for method isDivisibleBy7 """
        return cls.isDivisibleBy7(num / 10 - 2 * (num - num / 10 * 10))

