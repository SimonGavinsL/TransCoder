#!/usr/bin/env python
""" generated source for module if__0__SQUARE_ROOT_OF_AN_INTEGER_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def floorSqrt(cls, x):
        """ generated source for method floorSqrt """
        start = 1
        end = x
        ans = 0
        while start <= end:
            if mid * mid == x:
                return mid
            if mid * mid < x:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans

