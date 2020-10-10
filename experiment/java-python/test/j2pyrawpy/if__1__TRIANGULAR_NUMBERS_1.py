#!/usr/bin/env python
""" generated source for module if__1__TRIANGULAR_NUMBERS_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def isTriangular(cls, num):
        """ generated source for method isTriangular """
        c = (-2 * num)
        b = 1
        a = 1
        d = (b * b) - (4 * a * c)
        root1 = (-b + (Math.sqrt(d))) / (2 * a)
        root2 = (-b - (Math.sqrt(d))) / (2 * a)
        if root1 > 0 and Math.floor(root1) == root1:
            return True
        if root2 > 0 and Math.floor(root2) == root2:
            return True
        return False

