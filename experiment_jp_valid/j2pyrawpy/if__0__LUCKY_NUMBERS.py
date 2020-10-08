#!/usr/bin/env python
""" generated source for module if__0__LUCKY_NUMBERS """
class X(object):
    """ generated source for class X """
    @classmethod
    def isLucky(cls, n):
        """ generated source for method isLucky """
        next_position = n
        if n % counter == 0:
            return False
        next_position -= next_position / counter
        counter += 1
        return cls.isLucky(next_position)

