#!/usr/bin/env python
""" generated source for module for__0__SCHEDULE_JOBS_SERVER_GETS_EQUAL_LOAD """
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
            if a[i] > x:
                return -1
            if i > 0:
                a[i] += b[i - 1]
                b[i - 1] = 0
            if a[i] == x:
                continue 
            if i + 1 < n:
                y += b[i + 1]
            if y == x:
                a[i] = y
                b[i] = 0
                continue 
            if a[i] + b[i] == x:
                a[i] += b[i]
                b[i] = 0
                continue 
            if i + 1 < n and a[i] + b[i + 1] == x:
                a[i] += b[i + 1]
                b[i + 1] = 0
                continue 
            return -1
            i += 1
        while i < n:
            i += 1
        return x

