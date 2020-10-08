#!/usr/bin/env python
""" generated source for module while__0__JUMP_SEARCH """
class X(object):
    """ generated source for class X """
    @classmethod
    def jumpSearch(cls, arr, x):
        """ generated source for method jumpSearch """
        n = arr.length
        step = (Math.floor(Math.sqrt(n)))
        prev = 0
        while arr[prev] < x:
            prev += 1
            if prev == Math.min(step, n):
                return -1
        return -1

