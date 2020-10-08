#!/usr/bin/env python
""" generated source for module for__0__HOW_TO_PRINT_MAXIMUM_NUMBER_OF_A_USING_GIVEN_FOUR_KEYS """
class X(object):
    """ generated source for class X """
    @classmethod
    def findoptimal(cls, N):
        """ generated source for method findoptimal """
        if N <= 6:
            return N
        screen = [None]*N
        b = int()
        n = int()
        while n <= N:
            screen[n - 1] = Math.max(2 * screen[n - 4], Math.max(3 * screen[n - 5], 4 * screen[n - 6]))
            n += 1
        return screen[N - 1]

