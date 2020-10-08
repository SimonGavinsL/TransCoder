#!/usr/bin/env python
""" generated source for module for__0__REARRANGE_BINARY_STRING_ALTERNATE_X_Y_OCCURRENCES """
class X(object):
    """ generated source for class X """
    @classmethod
    def arrangeString(cls, str_, x, y):
        """ generated source for method arrangeString """
        count_0 = 0
        count_1 = 0
        len = len(str_)
        while count_0 > 0 or count_1 > 0:
            while j < x and count_0 > 0:
                if count_0 > 0:
                    print "0",
                    count_0 -= 1
                j += 1
            while j < y and count_1 > 0:
                if count_1 > 0:
                    print "1",
                    count_1 -= 1
                j += 1

