#!/usr/bin/env python
""" generated source for module if__0__DYNAMIC_PROGRAMMING_SET_36_CUT_A_ROPE_TO_MAXIMIZE_PRODUCT_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def maxProd(cls, n):
        """ generated source for method maxProd """
        res = 1
        while n > 4:
            n -= 3
            res *= 3
        return (n * res)

