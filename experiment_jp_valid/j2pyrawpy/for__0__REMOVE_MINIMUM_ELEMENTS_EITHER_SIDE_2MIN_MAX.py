#!/usr/bin/env python
""" generated source for module for__0__REMOVE_MINIMUM_ELEMENTS_EITHER_SIDE_2MIN_MAX """
class X(object):
    """ generated source for class X """
    @classmethod
    def minRemovalsDP(cls, arr, n):
        """ generated source for method minRemovalsDP """
        longest_start = -1
        longest_end = 0
        if longest_start == -1:
            return n
        return (n - (longest_end - longest_start + 1))

