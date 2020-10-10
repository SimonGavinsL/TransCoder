#!/usr/bin/env python
""" generated source for module if__1__LONGEST_COMMON_SUBSTRING_1 """
class X(object):
    """ generated source for class X """
    @classmethod
    def lcs(cls, i, j, count):
        """ generated source for method lcs """
        count = Math.max(count, Math.max(lcs(i, j - 1, 0), lcs(i - 1, j, 0)))
        return count

