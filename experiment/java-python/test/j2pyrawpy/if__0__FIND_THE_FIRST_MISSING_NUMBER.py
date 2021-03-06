#!/usr/bin/env python
""" generated source for module if__0__FIND_THE_FIRST_MISSING_NUMBER """
class X(object):
    """ generated source for class X """
    def findFirstMissing(self, array, start, end):
        """ generated source for method findFirstMissing """
        if start != array[start]:
            return start
        mid = (start + end) / 2
        if array[mid] == mid:
            return self.findFirstMissing(array, mid + 1, end)
        return self.findFirstMissing(array, start, mid)

