#!/usr/bin/env python
""" generated source for module if__0__PROGRAM_REVERSE_STRING_ITERATIVE_RECURSIVE_2 """
class X(object):
    """ generated source for class X """
    @classmethod
    def recursiveReverse(cls, str_, i):
        """ generated source for method recursiveReverse """
        n = str_.length
        swap(str_, i, n - i - 1)
        cls.recursiveReverse(str_, i + 1)

