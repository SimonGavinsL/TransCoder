#!/usr/bin/env python
""" generated source for module for__1__SCHEDULE_JOBS_SERVER_GETS_EQUAL_LOAD """
class X(object):
    """ generated source for class X """
    @classmethod
    def solve(cls, a, b, n):
        """ generated source for method solve """
        i = int()
        s = 0
        if n == 1:
            return a[0] + b[0]
        if s % n != 0:
            return -1
        x = s / n
        while i < n:
            i += 1
        return x

