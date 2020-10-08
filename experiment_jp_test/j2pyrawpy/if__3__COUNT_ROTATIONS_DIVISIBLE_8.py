#!/usr/bin/env python
""" generated source for module if__3__COUNT_ROTATIONS_DIVISIBLE_8 """
class X(object):
    """ generated source for class X """
    @classmethod
    def countRotationsDivBy8(cls, n):
        """ generated source for method countRotationsDivBy8 """
        len = len(n)
        count = 0
        threeDigit = int()
        threeDigit = (n.charAt(len - 1) - '0') * 100 + (n.charAt(0) - '0') * 10 + (n.charAt(1) - '0')
        threeDigit = (n.charAt(len - 2) - '0') * 100 + (n.charAt(len - 1) - '0') * 10 + (n.charAt(0) - '0')
        return count

