#!/usr/bin/env python
""" generated source for module for__0__FIND_NUMBER_ENDLESS_POINTS """
class X(object):
    """ generated source for class X """
    @classmethod
    def countEndless(cls, input, n):
        """ generated source for method countEndless """
        row = [None]*n
        col = [None]*n
        i = 0
        while i < n:
            while j >= 0:
                if input[i][j] == False:
                    isEndless = False
                row[i][j] = isEndless
                j -= 1
            i += 1
        ans = 0
        i = 0
        while i < n:
            i += 1
        return ans

