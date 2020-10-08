#!/usr/bin/env python
""" generated source for module for__0__FIND_THE_ELEMENT_THAT_APPEARS_ONCE_2 """
class X(object):
    """ generated source for class X """
    @classmethod
    def singleNumber(cls, a, n):
        """ generated source for method singleNumber """
        s = HashSet()
        arr_sum = 0
        for i in a:
            arr_sum += i
        set_sum = 0
        for i in s:
            set_sum += i
        return (3 * set_sum - arr_sum) / 2

